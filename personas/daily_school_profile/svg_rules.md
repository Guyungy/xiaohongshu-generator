# “每日一校”SVG 设计规范

## 1. 基础格式 (SVG Format)

- **纯矢量代码**: 必须是纯粹的 SVG 矢量代码。严禁包含任何光栅图像（如 PNG, JPG）。
- **Figma 兼容性**: 严禁使用 `<foreignObject>` 或嵌入 HTML/CSS。必须完全使用原生 SVG 标签（如 `<text>`, `<rect>`, `<line>`, `<path>`, `<g>`）来构建内容。这是为了确保 SVG 文件被拖入 Figma 后，所有的文字块和色块形状都可以被独立选中和编辑。

## 2. 尺寸与布局 (Dimensions & Layout)

- **单页比例**: `3:4` 竖屏。
- **单页像素**: `1080px` (宽) × `1440px` (高)。
- **输出形式**: **长图模式 (Long Image)**。所有页面在一个 SVG 文件中垂直排列。例如，一个 4 页的内容，最终输出的 SVG 文件尺寸应为 `1080px` × `5760px` (`1440px * 4`)。

## 3. 字体设定 (Typography)

- **中文优先**: **PingFang SC (苹方)**。这是保证在苹果生态系统下视觉效果统一的首选字体。
- **英文/数字**: **Arial** 或 **Georgia**。Arial 用于常规内容，Georgia 可用于需要特别强调的数字或引言，以增加经典感。
- **字体要求**: 确保所选字体在大多数主流操作系统下是通用的，避免因用户缺少字体而导致的显示错乱。

## 4. 视觉设计规范 (Visual Identity)

- **核心调性**: **英伦学院风 (British Academic Style)** —— 营造高端、严谨、专业、精英的视觉感受。

- **色彩系统 (Color System)** - **严格执行**:
    - **主色 (Authority/Base)**: `#0F1E3C` (深海军蓝 / Royal Navy Blue)。用于大标题、核心背景、图表主色。
    - **辅助色 (Highlight/Accent)**: `#D4AF37` (香槟金 / Champagne Gold)。用于图标、边框、引言、特殊数据点缀。
    - **背景色 (Paper/Canvas)**: `#F9F9F7` (米白 / Off-white)。用作内容区域的主背景，营造纸张质感，避免使用刺眼的纯白 `#FFFFFF`。
    - **警示色 (Warning/Emphasis)**: `#991B1B` 或 `#9A3412` (深红/砖红)。用于指出“误区”、“注意”、“避坑”等警示性内容。
    - **次级强调 (Secondary Accent)**: `#0369A1` (科技蓝)。用于与理科、科技、数据相关的图表或内容模块，作为深海军蓝的补充。

## 5. 排版原则 (Layout Principles)

- **高密度信息流**: 设计应模拟深度研究报告或高端财经杂志的版式。拒绝大面积无意义的留白，用有价值的“干货”内容填满画面。
- **结构化呈现**:
    - 多使用 **列表** (Bulleted/Numbered Lists)。
    - 多使用 **对比表格** (Comparison Tables)。
    - 多使用 **雷达图** (Radar Charts)、**数据胶囊** (Data Capsules)、**卡片式容器** (Card Containers) 来组织和呈现信息，使其更具结构感和易读性。
- **页眉/页脚 (Header/Footer)**:
    - **页眉**: 每页的顶部必须包含一个品牌栏目条，内容为 `TONGXIANG YEW WAH EDU-DAILY` 或类似标识。
    - **页脚**: 每页的底部必须包含页码，格式为 `01 / 04` (当前页 / 总页数)。
