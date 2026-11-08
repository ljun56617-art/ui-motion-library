const spring = {
  // 跟手弹簧：拖拽松手类效果共用的三个小工具，无依赖，整段带走即可。
  // 用法：按下时 t = spring.tracker()，移动时 t.add(位置)，松手时 v = t.speed()，再 spring.to(当前位置, 终点, v, 画)。
  //
  // spring.to(from, to, v, draw, opt, done)：用弹簧把数值从 from 带到 to。
  //   没有写死的时长：每帧按「刚度 × 距离 − 阻尼 × 速度」算加速度，位置和速度都够小时自己停。
  //   v          起始速度，单位「每秒多少」，一般填松手速度，这样轻划和猛甩出来的动作不一样；填 0 就是从静止出发
  //   draw(x, v) 每帧调用一次，拿 x 去改样式
  //   opt.stiffness 刚度，默认 300。调大：拉得更狠，更快到、更干脆；调小：慢悠悠、发软
  //   opt.damping   阻尼比，默认 1。等于 1：最快停稳、不来回晃（猛甩时可能冲过终点一次再回来）；
  //                 小于 1：冲过头再晃回来，越小晃得越多，0.5 大约晃两下，适合俏皮的地方；大于 1：像在糖浆里慢慢挪
  //   opt.mass      质量，默认 1。调大：更沉，惯性更大，同样一甩冲得更远、停得更慢；调小：更轻、更灵
  //   opt.rest      停下的门槛，默认 0.1（适合 px）。scale 这类很小的数要调小，比如 0.001
  //   返回一个函数，调用它可以中途停下（手指再次按住时用）。
  //   开了系统的「减少动态效果」（prefers-reduced-motion）时直接跳到终点。
  to(from, to, v, draw, opt = {}, done) {
    const k = opt.stiffness ?? 300, m = opt.mass ?? 1, rest = opt.rest ?? .1;
    const c = 2 * (opt.damping ?? 1) * Math.sqrt(k * m);
    let x = from, raf = 0, stopped = false, last = performance.now();
    const finish = () => { draw(to, 0); if (done) done(); };
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) { finish(); return () => {}; }
    const step = (now) => {
      // Fixed 4 ms sub-steps keep stiff springs stable even when a frame arrives late.
      for (let dt = Math.min(.064, (now - last) / 1000); dt > 0; dt -= .004) {
        const h = Math.min(dt, .004);
        v += (-k * (x - to) - c * v) / m * h;
        x += v * h;
      }
      last = now;
      if (Math.abs(x - to) < rest && Math.abs(v) < rest * 10) { finish(); return; }
      draw(x, v);
      if (!stopped) raf = requestAnimationFrame(step);
    };
    raf = requestAnimationFrame(step);
    return () => { stopped = true; cancelAnimationFrame(raf); };
  },
  // spring.rubber(x, min, max, size, c)：橡皮筋。x 在 min 到 max 之间原样返回；拉出边界后越拉越拉不动。
  //   size  元素在拖动方向上的尺寸（px），拉出去的距离永远到不了它
  //   c     阻力系数，默认 0.55（iOS 的取值）。调小：边界更硬，几乎拉不动；调大（最多 1）：更松
  rubber(x, min, max, size, c = .55) {
    const band = (d) => (1 - 1 / (d * c / size + 1)) * size;
    return x < min ? min - band(min - x) : x > max ? max + band(x - max) : x;
  },
  // spring.tracker()：估算松手速度。add(x) 记下每次指针位置，speed() 用最近 100ms 的位移算出每秒多少 px。
  //   松手前手指停住超过 80ms，速度算 0，这样「拖过去停一下再松」不会被当成甩。
  tracker() {
    let pts = [];
    return {
      add(x) {
        const t = performance.now();
        pts.push([t, x]);
        while (pts.length > 2 && t - pts[0][0] > 100) pts.shift();
      },
      speed() {
        const a = pts[0], b = pts[pts.length - 1];
        pts = [];
        if (!a || b[0] - a[0] < 1 || performance.now() - b[0] > 80) return 0;
        return (b[1] - a[1]) / (b[0] - a[0]) * 1000;
      },
    };
  },
};
