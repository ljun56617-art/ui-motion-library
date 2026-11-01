# UI 动效库目录

共 133 种效果，每行一种。第一列是「页面/编号」，最后一列是可以直接打开运行的单文件，相对本目录。

这个文件由 src/build.py 生成，不要手改。

| 编号 | 场景 | 名称 | 英文 | 什么时候用 | 关键参数 | 代码 |
|---|---|---|---|---|---|---|
| 01-buttons/01 | 分清主次 | 主按钮 | Primary Button | 一屏里最该被点的那个，一个区域通常只放一个，比如「提交」。 |  | snippets/01-buttons/01-主按钮.html |
| 01-buttons/02 | 分清主次 | 次按钮 | Secondary Button | 陪在主按钮旁边的备选项，比如「取消」，颜色要退后一步。 |  | snippets/01-buttons/02-次按钮.html |
| 01-buttons/03 | 分清主次 | 线框按钮 | Outline Button | 透明底加一圈描边，分量介于次按钮和文字按钮之间。 |  | snippets/01-buttons/03-线框按钮.html |
| 01-buttons/04 | 分清主次 | 文字按钮 | Text Button | 看起来几乎就是一段文字，用在「忘记密码」这类偶尔才点的入口。 |  | snippets/01-buttons/04-文字按钮.html |
| 01-buttons/05 | 分清主次 | 幽灵按钮 | Ghost Button | 压在图片或彩色背景上也不抢画面，鼠标过来才现出底色。 |  | snippets/01-buttons/05-幽灵按钮.html |
| 01-buttons/06 | 分清主次 | 胶囊按钮 | Pill Button | 圆角拉满，观感柔和，手机界面和标签样式里很常见。 |  | snippets/01-buttons/06-胶囊按钮.html |
| 01-buttons/07 | 防止手滑 | 危险按钮 | Danger Button | 删除、注销这种做了就撤不回的动作，用红色提醒用户看清楚。 |  | snippets/01-buttons/07-危险按钮.html |
| 01-buttons/08 | 防止手滑 | 长按确认按钮 | Press and Hold | 删除、清空这类手滑会后悔的操作。比弹窗确认更快，也不容易误触。 |  | snippets/01-buttons/08-长按确认按钮.html |
| 01-buttons/09 | 防止手滑 | 滑动确认 | Slide to Confirm | 付款、解锁这类要用户明确同意的动作。手机上单手就能完成。 |  | snippets/01-buttons/09-滑动确认.html |
| 01-buttons/10 | 一处放多个操作 | 图标按钮 | Icon Button | 收藏、下载这类看图标就明白的动作，占地很小。 |  | snippets/01-buttons/10-图标按钮.html |
| 01-buttons/11 | 一处放多个操作 | 按钮组 | Button Group | 几个有关联的动作拼成一整条，比如上一页、今天、下一页。 |  | snippets/01-buttons/11-按钮组.html |
| 01-buttons/12 | 一处放多个操作 | 分割按钮 | Split Button | 左半边直接执行常用动作，右半边的箭头收着其他选择。 |  | snippets/01-buttons/12-分割按钮.html |
| 01-buttons/13 | 一处放多个操作 | 悬浮按钮 | Floating Action Button | 悬在页面角落不随内容滚走，留给发布这种最常用的动作。 |  | snippets/01-buttons/13-悬浮按钮.html |
| 01-buttons/14 | 让按钮有反应 | 默认状态 | Default | 按钮没被碰时的样子。这张卡里的按钮可以直接操作，试一遍后面几种状态。 |  | snippets/01-buttons/14-默认状态.html |
| 01-buttons/15 | 让按钮有反应 | 悬停状态 | Hover | 光标一到就有变化，告诉用户这里能点。卡片里把这个瞬间定住了。 |  | snippets/01-buttons/15-悬停状态.html |
| 01-buttons/16 | 让按钮有反应 | 按下状态 | Active / Pressed | 手指或鼠标按住的那一下会往里收，让人觉得真的按到了。卡片里同样定住了。 |  | snippets/01-buttons/16-按下状态.html |
| 01-buttons/17 | 让按钮有反应 | 焦点状态 | Focus | 用 Tab 键走到这里时亮起的外框，只用键盘的人靠它知道自己在哪。 |  | snippets/01-buttons/17-焦点状态.html |
| 01-buttons/18 | 让按钮有反应 | 加载与成功状态 | Loading & Success | 等结果时转圈、不让再点，结果回来后换成对勾。 |  | snippets/01-buttons/18-加载与成功状态.html |
| 01-buttons/19 | 让按钮有反应 | 禁用状态 | Disabled | 暂时不能点，颜色发灰，最好再写明差什么条件。 |  | snippets/01-buttons/19-禁用状态.html |
| 01-buttons/20 | 让按钮有反应 | 涟漪按钮 | Ripple Button | 让用户确认「点到了」，手机上尤其有用。水波从手指落点散开。 |  | snippets/01-buttons/20-涟漪按钮.html |
| 01-buttons/21 | 让用户做选择 | 开关 | Switch | 一拨就生效，不需要「保存」，深色模式这种设置正合适。 |  | snippets/01-buttons/21-开关.html |
| 01-buttons/22 | 让用户做选择 | 切换按钮 | Toggle Button | 只有开和关两种样子，点赞、收藏都是这个逻辑。 |  | snippets/01-buttons/22-切换按钮.html |
| 01-buttons/23 | 让用户做选择 | 复选框 | Checkbox | 可以勾好几个，一般等点了保存才算数。 |  | snippets/01-buttons/23-复选框.html |
| 01-buttons/24 | 让用户做选择 | 单选框 | Radio | 一组里只留一个，选中新的，旧的跟着取消。 |  | snippets/01-buttons/24-单选框.html |
| 01-buttons/25 | 让用户做选择 | 可选标签 | Chip | 小胶囊排成一行，点一下选中，再点取消，筛选时常用。 |  | snippets/01-buttons/25-可选标签.html |
| 01-buttons/26 | 让用户做选择 | 分段控制器 | Segmented Control | 两三个互斥选项挤在一条里，一个色块滑到当前项，很省地方。 |  | snippets/01-buttons/26-分段控制器.html |
| 01-buttons/27 | 让用户做选择 | 计数器 | Stepper | 加减号夹着一个数字，改购物车件数就用它。 |  | snippets/01-buttons/27-计数器.html |
| 02-modals/01 | 必须先处理 | 弹窗 | Modal | 压在页面正中，背后整页变暗。能用叉、遮罩或 Esc 键退出。 |  | snippets/02-modals/01-弹窗.html |
| 02-modals/02 | 必须先处理 | 确认弹窗 | Alert Dialog | 动手前再问一遍，点遮罩也关不掉，非选一个不可。 |  | snippets/02-modals/02-确认弹窗.html |
| 02-modals/03 | 必须先处理 | 气泡确认框 | Popover Confirm | 贴着按钮问一句「确定吗」，不遮挡整个页面，适合风险不大的操作。 |  | snippets/02-modals/03-气泡确认框.html |
| 02-modals/04 | 展开更多内容 | 抽屉 | Drawer | 从一侧推出来的长面板，背后页面还在，适合对照着内容做设置。 |  | snippets/02-modals/04-抽屉.html |
| 02-modals/05 | 展开更多内容 | 底部弹层 | Bottom Sheet | 贴着手机屏幕底边升起来，大拇指够得着。 |  | snippets/02-modals/05-底部弹层.html |
| 02-modals/06 | 展开更多内容 | 下拉菜单 | Dropdown Menu | 按钮底下展开一串命令，把不常用的动作收起来。 |  | snippets/02-modals/06-下拉菜单.html |
| 02-modals/07 | 展开更多内容 | 气泡卡片 | Popover | 点了才出来的小卡片，放得下头像、文字，还能放按钮。 |  | snippets/02-modals/07-气泡卡片.html |
| 02-modals/08 | 展开更多内容 | 灯箱 | Lightbox | 看大图。图片从原来的位置放大出来，用户知道它从哪来、回哪去。 |  | snippets/02-modals/08-灯箱.html |
| 02-modals/09 | 提醒一下就走 | 轻提示 | Toast | 一句话的回执，比如「已保存」，停一两秒就走，不需要用户动手。 |  | snippets/02-modals/09-轻提示.html |
| 02-modals/10 | 提醒一下就走 | 通知 | Notification | 比轻提示块头大、留得久，有标题和关闭按钮，用于不能错过的消息。 |  | snippets/02-modals/10-通知.html |
| 02-modals/11 | 提醒一下就走 | 气泡提示 | Tooltip | 光标停在图标上时冒出一句解释，内容只作补充，重要的话别放这里。 |  | snippets/02-modals/11-气泡提示.html |
| 03-motion/01 | 元素出现和离开 | 淡入淡出 | Fade | 最省事也最不会出错的过渡，内容出现、消失都能用。 | 200–300ms · ease-in-out · opacity | snippets/03-motion/01-淡入淡出.html |
| 03-motion/02 | 元素出现和离开 | 滑入 | Slide In | 内容有方向感：从哪来、往哪去。轮播、页面切换常用。 | 300ms · ease-out · translateX | snippets/03-motion/02-滑入.html |
| 03-motion/03 | 元素出现和离开 | 缩放 | Scale / Zoom | 弹窗、图标出现时用。从小变大，视线会自然落在中间。 | 300ms · 回弹 cubic-bezier · scale | snippets/03-motion/03-缩放.html |
| 03-motion/04 | 元素出现和离开 | 翻转 | 3D Flip | 正反两面切换，比如单词卡、答题揭晓。 | 700ms · perspective 700px · rotateY | snippets/03-motion/04-翻转.html |
| 03-motion/05 | 元素出现和离开 | 错峰 | Stagger | 列表不是一起出现，而是一项接一项，视线会顺着往下走。 | 每项延迟 90ms · ease-out · translateY | snippets/03-motion/05-错峰.html |
| 03-motion/06 | 元素出现和离开 | 弹性 | Spring | 先过头一点再退回来，带果冻的质感，适合轻松的界面。 | 过冲 1.16 → 回弹 0.93 → 稳定 | snippets/03-motion/06-弹性.html |
| 03-motion/07 | 元素出现和离开 | 缓动 | Easing | 决定动作快慢怎么变化，先快后慢最接近真实物体。这里三条线同时起跑，可以直接对比。 | linear / ease-in / ease-out | snippets/03-motion/07-缓动.html |
| 03-motion/08 | 突出卡片和按钮 | 悬停上浮 | Hover Lift | 卡片被光标碰到时抬起一点，阴影也跟着加重，暗示它能点。 | 200ms · translateY -7px · 阴影加深 | snippets/03-motion/08-悬停上浮.html |
| 03-motion/09 | 突出卡片和按钮 | 聚光 | Spotlight | 光斑跟着光标在卡片上移动，边框也会在光标附近亮起。 | 径向渐变 · CSS 变量记鼠标坐标 | snippets/03-motion/09-聚光.html |
| 03-motion/10 | 突出卡片和按钮 | 3D 倾斜 | Tilt | 卡片朝光标的方向偏转，有一点立体的手感。 | 最大 14° · perspective 800px | snippets/03-motion/10-3D-倾斜.html |
| 03-motion/11 | 突出卡片和按钮 | 磁吸 | Magnetic | 光标靠近，按钮主动往光标那边偏一点，离开后弹回。 | 感应半径 110px · 吸附 35% · 弹性归位 | snippets/03-motion/11-磁吸.html |
| 03-motion/12 | 突出卡片和按钮 | 边缘流光 | Border Beam | 光点绕着卡片的边走，从不停下，放在想让人先看的那张卡上。 | 3s 一圈 · linear · conic-gradient | snippets/03-motion/12-边缘流光.html |
| 03-motion/13 | 突出卡片和按钮 | 流光 | Shimmer | 一条亮带斜着划过去，常加在想让人点的按钮上，骨架屏也用得上。 | 2.6s · ease-in-out · 倾斜 22° 的高光带 | snippets/03-motion/13-流光.html |
| 03-motion/14 | 跟着滚动变化 | 滚动出现 | Scroll Reveal | 元素滑到视口里才现身，长页面读起来不至于一次全堆在眼前。 | IntersectionObserver · 450ms · translateY | snippets/03-motion/14-滚动出现.html |
| 03-motion/15 | 跟着滚动变化 | 视差滚动 | Parallax | 前后几层以不同速度移动，近快远慢，页面就有了景深。 | 远景慢、近景快 · translateY | snippets/03-motion/15-视差滚动.html |
| 03-motion/16 | 跟着滚动变化 | 滚动叙事 | Scroll Storytelling | 画面钉在屏幕上，下滑时里面的内容分步切换，适合讲产品流程。 | position: sticky · 按滚动进度切步骤 | snippets/03-motion/16-滚动叙事.html |
| 03-motion/17 | 文字和数字 | 打字机 | Typewriter | 字一个接一个冒出来，末尾一条光标在闪，AI 回复和大标题都常用。 | 每字 70ms · 光标 1s 闪烁 | snippets/03-motion/17-打字机.html |
| 03-motion/18 | 文字和数字 | 乱码解码 | Scramble Text | 先闪过一串随机字符，再一个字一个字落定，常用于标题。 | 每字 60ms 定格 · 等宽字体 | snippets/03-motion/18-乱码解码.html |
| 03-motion/19 | 文字和数字 | 数字滚动 | Count Up | 从 0 一路跳到目标数，比静止的数字更容易吸引目光。 | 1600ms · ease-out · 等宽数字 | snippets/03-motion/19-数字滚动.html |
| 03-motion/20 | 文字和数字 | 跑马灯 | Marquee | 内容排成一行不停往一边走，放 Logo 墙很合适。 | 16s 一轮 · linear · 复制一份无缝衔接 | snippets/03-motion/20-跑马灯.html |
| 03-motion/21 | 提醒和装饰 | 弹跳 | Bounce | 活泼的提示，引导往下滑、提示点这里。落地时压扁才有重量感。 | 1.5s · 落地压扁 1.25 / 0.72 · 循环 | snippets/03-motion/21-弹跳.html |
| 03-motion/22 | 提醒和装饰 | 抖动 | Shake | 告诉用户「不对」。密码错误时输入框左右摇一下，像人在摇头。 | 400ms · 位移衰减 9→2px · translateX | snippets/03-motion/22-抖动.html |
| 03-motion/23 | 提醒和装饰 | 脉冲 | Pulse | 新消息红点、直播中的标记。一圈圈往外散，安静地提醒。 | 1.8s · ease-out · scale + opacity · 两圈错开 | snippets/03-motion/23-脉冲.html |
| 03-motion/24 | 提醒和装饰 | 变形 | Morph | 同一个元素变成另一种形状，常见于菜单图标、背景装饰。 | 5.2s · ease-in-out · border-radius + rotate | snippets/03-motion/24-变形.html |
| 03-motion/25 | 提醒和装饰 | 线条描绘 | SVG Line Draw | Logo 开场、流程图讲解。线条像被一笔笔画出来。 | stroke-dashoffset · pathLength=1 · 2.2s | snippets/03-motion/25-线条描绘.html |
| 04-forms/01 | 填内容和传文件 | 输入框和提交按钮 | Input & Submit | 表单的最小组合，AI 不用提示也做得出来，一般不必多说。 |  | snippets/04-forms/01-输入框和提交按钮.html |
| 04-forms/02 | 填内容和传文件 | 浮动标签 | Floating Label | 字段名先待在框里，一点进去就缩到框的上沿，填的时候也不会丢。 |  | snippets/04-forms/02-浮动标签.html |
| 04-forms/03 | 填内容和传文件 | 搜索框 | Search Field | 平时收得短，点进去才展开。有内容时才出现清空按钮。 |  | snippets/04-forms/03-搜索框.html |
| 04-forms/04 | 填内容和传文件 | 自增高文本域 | Auto-grow Textarea | 写长文字时框跟着变高，不出现内部滚动条。右下角提示还能写多少字。 |  | snippets/04-forms/04-自增高文本域.html |
| 04-forms/05 | 填内容和传文件 | 标签输入 | Tag Input | 回车一次生成一个小标签，适合填多个关键词，删起来也方便。 |  | snippets/04-forms/05-标签输入.html |
| 04-forms/06 | 填内容和传文件 | 验证码输入框 | OTP Input | 每个数字一格，填完自动跳格，退格往回走，也能直接粘贴整串。 |  | snippets/04-forms/06-验证码输入框.html |
| 04-forms/07 | 填内容和传文件 | 拖拽上传 | Dropzone | 把文件拖进虚线区就开始传，每个文件有进度，传错了能删。 |  | snippets/04-forms/07-拖拽上传.html |
| 04-forms/08 | 从选项里选 | 下拉选择 | Select | 选项多时才收进下拉。只有三四个的话，直接铺开成单选框更好比较。 |  | snippets/04-forms/08-下拉选择.html |
| 04-forms/09 | 从选项里选 | 自动补全 | Autocomplete | 打几个字就列出匹配项，城市、学校这种选项太多的字段靠它。 |  | snippets/04-forms/09-自动补全.html |
| 04-forms/10 | 从选项里选 | 级联选择 | Cascader | 一级选完才出下一级，比如省、市、区。 |  | snippets/04-forms/10-级联选择.html |
| 04-forms/11 | 从选项里选 | 日期选择器 | Date Picker | 订酒店这种要选起止日期的场景最合适。生日就别用了，直接输入比翻月快得多。 |  | snippets/04-forms/11-日期选择器.html |
| 04-forms/12 | 从选项里选 | 滑块 | Slider | 拖两个把手定一个大致范围，比如价格。要准确数字就旁边再配输入框。 |  | snippets/04-forms/12-滑块.html |
| 04-forms/13 | 从选项里选 | 评分 | Rating | 打分、满意度。悬停预览，点击时星星依次弹一下，下面的文字跟着变。 |  | snippets/04-forms/13-评分.html |
| 04-forms/14 | 帮用户填对 | 必填星号 | Required | 字段名后面一个红星就够了，别把输入框都染红。 |  | snippets/04-forms/14-必填星号.html |
| 04-forms/15 | 帮用户填对 | 帮助文字 | Helper Text | 格子下面一行说明，一直在那里，比如密码要几位，不用等出错才知道。 |  | snippets/04-forms/15-帮助文字.html |
| 04-forms/16 | 帮用户填对 | 校验报错 | Validation | 等用户离开这一格再检查，错了就在格子底下写明该怎么改。 |  | snippets/04-forms/16-校验报错.html |
| 04-forms/17 | 帮用户填对 | 密码强度 | Password Strength | 边输边看强度条变色，眼睛图标能切换显示和隐藏。 |  | snippets/04-forms/17-密码强度.html |
| 05-loading/01 | 知道版式，在等内容 | 骨架屏 | Skeleton | 内容到之前先用灰块摆出版式，微光扫过，说明不是卡死。 |  | snippets/05-loading/01-骨架屏.html |
| 05-loading/02 | 知道版式，在等内容 | 模糊渐显 | Blur-up | 先铺一张糊的小图占住位置，大图到了再慢慢变清楚，不会突然跳一下。 |  | snippets/05-loading/02-模糊渐显.html |
| 05-loading/03 | 等得不久 | 加载动画 | Spinner | 转圈的基本款，AI 不用提示也会写。 |  | snippets/05-loading/03-加载动画.html |
| 05-loading/04 | 等得不久 | 圆环 | Ring Spinner | 最通用的加载圈：一圈浅色轨道，一段深色在上面转。 |  | snippets/05-loading/04-圆环.html |
| 05-loading/05 | 等得不久 | 渐变光环 | Conic Spinner | 圆环带一条会淡出的尾巴，比普通圆环精致，高级感来自颜色渐变。 |  | snippets/05-loading/05-渐变光环.html |
| 05-loading/06 | 等得不久 | 三点跳动 | Typing Dots | 对方正在回复。放在聊天气泡里，AI 对话产品几乎都用它。 |  | snippets/05-loading/06-三点跳动.html |
| 05-loading/07 | 等得不久 | 省略号 | Ellipsis | 放在文字后面最省事，一行字就能说明「还在加载」，不占地方。 |  | snippets/05-loading/07-省略号.html |
| 05-loading/08 | 等得不久 | 按钮加载状态 | Loading Button | 点完提交，按钮转圈且点不了，重复提交就不会发生。 |  | snippets/05-loading/08-按钮加载状态.html |
| 05-loading/09 | 等得不久 | 均衡器 | Equalizer | 语音、音频转写的场景。几根竖条依次起伏，一看就和声音有关。 |  | snippets/05-loading/09-均衡器.html |
| 05-loading/10 | 等得不久 | 轨道环绕 | Orbit | 两颗小球绕着中心反向转，看起来很忙，适合科技感的产品。 |  | snippets/05-loading/10-轨道环绕.html |
| 05-loading/11 | 等得不久 | 脉冲扩散 | Ping | 中心不动，圆圈一层层往外散，常用于「正在定位」「正在搜索附近」。 |  | snippets/05-loading/11-脉冲扩散.html |
| 05-loading/12 | 等得不久 | 方块翻转 | Flip Cube | 一个方块上下翻面，有厚度感，比转圈更有记忆点。 |  | snippets/05-loading/12-方块翻转.html |
| 05-loading/13 | 等得不久 | 弹跳球 | Bouncing Ball | 活泼的等待动画。影子跟着变大变小，球才像真的落在地上。 |  | snippets/05-loading/13-弹跳球.html |
| 05-loading/14 | 等得不久 | 九宫闪烁 | Grid Pulse | 九个小方块依次亮起，像一道波纹扫过，适合数据、仪表盘类页面。 |  | snippets/05-loading/14-九宫闪烁.html |
| 05-loading/15 | 等得久，要给进度感 | 进度条 | Progress Bar | 上传大文件这种耗时的活用它，完成多少、还差多久都看得到。 |  | snippets/05-loading/15-进度条.html |
| 05-loading/16 | 等得久，要给进度感 | 环形进度 | Circular Progress | 和进度条是同一件事，但占地小，适合放在卡片或按钮里。 |  | snippets/05-loading/16-环形进度.html |
| 05-loading/17 | 等得久，要给进度感 | 不确定进度条 | Indeterminate Progress | 不知道还要多久时用。一小段在轨道上来回走，只表示「还在忙」，不给百分比。 |  | snippets/05-loading/17-不确定进度条.html |
| 05-loading/18 | 等得久，要给进度感 | 斜纹滚动 | Barber Stripes | 像理发店灯柱，斜条纹一直往前走，动感强，等待时不显得卡住。 |  | snippets/05-loading/18-斜纹滚动.html |
| 05-loading/19 | 等得久，要给进度感 | 顶部细线加载条 | Top Loading Bar | 网页切换页面时贴着顶部走的那条线，存在感低，用户知道在动就行。 |  | snippets/05-loading/19-顶部细线加载条.html |
| 05-loading/20 | 等得久，要给进度感 | 加载文案轮播 | Loading Messages | AI 生成这种要等几十秒的任务。告诉用户正在做哪一步，等待就有了盼头。 |  | snippets/05-loading/20-加载文案轮播.html |
| 05-loading/21 | 等得久，要给进度感 | 品牌开屏 | Logo Splash | App 启动、大型页面首次打开。把等待时间用来露一次品牌。 |  | snippets/05-loading/21-品牌开屏.html |
| 05-loading/22 | 列表更新 | 下拉刷新 | Pull to Refresh | 手指往下拖，松开后顶上转一圈，新内容就到了。 |  | snippets/05-loading/22-下拉刷新.html |
| 05-loading/23 | 列表更新 | 无限滚动 | Infinite Scroll | 信息流。滑到底自动接着加载，用户不用点「下一页」。 |  | snippets/05-loading/23-无限滚动.html |
| 05-loading/24 | 列表更新 | 乐观更新 | Optimistic UI | 不等服务器回话就先显示成功，万一失败再退回去告诉用户，手感会很快。 |  | snippets/05-loading/24-乐观更新.html |
| 05-loading/25 | 出错和没内容 | 空状态 | Empty State | 列表没东西时别留白，说明为什么是空的，再给一个能点的下一步。 |  | snippets/05-loading/25-空状态.html |
| 05-loading/26 | 出错和没内容 | 404 页面 | Not Found | 页面找不到时的出口。语气可以轻松点，但一定要有回首页的按钮。 |  | snippets/05-loading/26-404-页面.html |
| 05-loading/27 | 出错和没内容 | 错误页 | Error Page | 服务器出问题时说清楚不是用户的错，给一个「重试」。 |  | snippets/05-loading/27-错误页.html |
| 05-loading/28 | 出错和没内容 | 断网提示 | Offline | 网断了顶部滑下一条提示，网回来后自己收起。 |  | snippets/05-loading/28-断网提示.html |
| 05-loading/29 | 出错和没内容 | 没有权限 | No Permission | 写清缺哪项权限、该找谁开，顺手放一个申请按钮。 |  | snippets/05-loading/29-没有权限.html |
| 05-loading/30 | 出错和没内容 | 结果页 | Result | 操作结束后的交代：成功就给下一步，失败就说明原因，并能回去改。 |  | snippets/05-loading/30-结果页.html |
| 06-cards/01 | 展示一项内容 | 基础信息卡 | Basic Card | 标题、一句说明、一个入口。所有卡片都是它的变种。 |  | snippets/06-cards/01-基础信息卡.html |
| 06-cards/02 | 展示一项内容 | 图文卡 | Media Card | 上图下文，图片负责吸引点击。悬停时只放大图片，外框不动。 |  | snippets/06-cards/02-图文卡.html |
| 06-cards/03 | 展示一项内容 | 个人资料卡 | Profile Card | 展示一个人。头像压在封面和内容的分界线上，是最常见的版式。 |  | snippets/06-cards/03-个人资料卡.html |
| 06-cards/04 | 展示一项内容 | 商品卡 | Product Card | 电商列表。价格要醒目，购买按钮悬停才滑出来，平时画面更干净。 |  | snippets/06-cards/04-商品卡.html |
| 06-cards/05 | 展示一项内容 | 价格卡 | Pricing Card | 让用户比较方案。推荐款放大并加描边，视线会先落到它上面。 |  | snippets/06-cards/05-价格卡.html |
| 06-cards/06 | 展示一项内容 | 统计卡片 | Stat Card | 一个醒目的大数字，加上涨跌方向，后台首页的常客。 |  | snippets/06-cards/06-统计卡片.html |
| 06-cards/07 | 展示一项内容 | 翻转卡片 | Flip Card | 光标一到，卡片转个面，一面是图，另一面是说明。 |  | snippets/06-cards/07-翻转卡片.html |
| 06-cards/08 | 展示一项内容 | 玻璃拟态卡 | Glassmorphism | 半透明磨砂，背后的色块透出来。背景要有色彩变化才看得出效果。 |  | snippets/06-cards/08-玻璃拟态卡.html |
| 06-cards/09 | 展示很多项 | 卡片和列表 | Card & List | 两种基础排法。图片重要用卡片，要快速看很多条用列表。 |  | snippets/06-cards/09-卡片和列表.html |
| 06-cards/10 | 展示很多项 | 瀑布流 | Masonry | 列宽一致、高矮不齐，图片比例不一样时也能排得紧密。 |  | snippets/06-cards/10-瀑布流.html |
| 06-cards/11 | 展示很多项 | 便当格 | Bento Grid | 大小不一的卡片拼成一块，把重点放大。近年官网和个人主页很流行。 |  | snippets/06-cards/11-便当格.html |
| 06-cards/12 | 展示很多项 | 轮播 | Carousel | 几张图轮流露面，通常占首页首屏的大块位置。 |  | snippets/06-cards/12-轮播.html |
| 06-cards/13 | 展示很多项 | 堆叠卡 | Stacked Cards | 空间有限又有多张内容时。下面露出的边提示「还有更多」。 |  | snippets/06-cards/13-堆叠卡.html |
| 06-cards/14 | 展示很多项 | 滑动卡 | Swipe Card | 一次只决定一张，左滑不要、右滑想要。探探模式。 |  | snippets/06-cards/14-滑动卡.html |
| 06-cards/15 | 标注和收纳 | 时间线 | Timeline | 竖线上串几个节点，快递走到哪一站这类记录一眼能看懂。 |  | snippets/06-cards/15-时间线.html |
| 06-cards/16 | 标注和收纳 | 徽标 | Badge | 角上的红点或小数字，说明有新东西。数字太大就写 99+。 |  | snippets/06-cards/16-徽标.html |
| 06-cards/17 | 标注和收纳 | 标签 | Tag | 小色块标出状态。状态多时别每种都配新色，五种上下最好认。 |  | snippets/06-cards/17-标签.html |
| 06-cards/18 | 标注和收纳 | 头像组 | Avatar Group | 圆头像叠着排，尾巴写「+5」，表示还有几个人一起。 |  | snippets/06-cards/18-头像组.html |
| 06-cards/19 | 标注和收纳 | 折叠面板 | Accordion | 标题常驻，内容点开才看，常见问题列表和手机页面很合适。 |  | snippets/06-cards/19-折叠面板.html |
| 06-cards/20 | 长表格 | 固定表头 | Fixed Header | 数据再长，列名都钉在最上面，不用翻回去对。 |  | snippets/06-cards/20-固定表头.html |
| 06-cards/21 | 长表格 | 斑马纹 | Zebra Stripes | 隔行换个底色，眼睛不容易看错行。金额靠右对齐，大小才好比较。 |  | snippets/06-cards/21-斑马纹.html |
| 06-cards/22 | 长表格 | 排序和筛选 | Sort & Filter | 点表头换顺序，点漏斗缩小范围，数据多时必备。 |  | snippets/06-cards/22-排序和筛选.html |
| 06-cards/23 | 长表格 | 行内操作 | Row Actions | 编辑、删除收在行尾，光标经过才露出来，表格看着清爽。 |  | snippets/06-cards/23-行内操作.html |
