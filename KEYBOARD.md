# SublimeText(4128) 快捷键

## 文件(File)
+ Ctrl + N: 在当前窗口创建一个新标签
+ Ctrl + O: 打开文件
+ Ctrl + Shift + T: 重新打开最近关闭的文件
+ Ctrl + S: 保存
+ Ctrl + Shift + S: 另存为
+ Ctrl + Shift + N: 创建一个新窗口
+ Ctrl + Shift + W: 关闭窗口
+ Ctrl + W: 关闭当前标签，当窗口内没有标签时会关闭该窗口

## 编辑(Editing)
+ Ctrl + Z: 撤销，针对文字编辑而言
+ Ctrl + Y: 恢复撤销，针对文字编辑而言
+ Ctrl + U: 软撤销,不只针对文字编辑，额外的针对选择文本一样
+ Ctrl + Shift + U: 软反撤销
+ Ctrl + X: 剪切所选内容至剪切板中，如果没有选择内容，则剪切光标所在行
+ Ctrl + C: 复制所选内容至剪切板中，如果没有选择内容，则复制光标所在行
+ Ctrl + V: 粘贴
+ Ctrl + Shift + V: 缩进粘贴
+ Ctrl + K + V: 从历史剪切板中粘贴
+ Ctrl + ]: 增加缩进
+ Ctrl + [: 减少缩进
+ Ctrl + Shift + ↑: 向下交换一行
+ Ctrl + Shift + ↓: 向上交换一行
+ Ctrl + Shift + D: 复制光标所在行并插入到下一行
+ Ctrl + Shift + K: 删除选中的行，如果没有选中，则删除光标所在行
+ Ctrl + Shift + J: 合并选中的多行为一行
+ Ctrl + /: 单行注释，注释选择的多行
+ Ctrl + Shift + /: 多行注释
+ Ctrl + K + Z: 还原修改
+ Ctrl + K, Ctrl + Shift + Z:
+ Ctrl + K + /: 显示内嵌差异块
+ Ctrl + Enter: 在当前行下面新增一行然后跳至该行
+ Ctrl + Shift + Enter: 在当前行上面增加一行并跳至该行
+ Ctrl + Delete: 删除下一个单词
+ Ctrl + Backspace 删除上一个单词
+ Ctrl + K + K: 从光标处开始删除代码至行尾(Ctrl + Shift + Delete)
+ Ctrl + K + Backspace: 删除到行首(Ctrl + Shift + Backspace)
+ Ctrl + T: 交换光标前后字母/文字
+ Alt + .: 关闭HTML标签
+ Ctrl + Shift + A: 扩展选择当前内容至HTML标签
+ Alt + Shift + W: 用标签包围所选内容(作用未知，异常退出)
+ Ctrl + K + Space: 设置标记（此快捷键不起作用）
+ Ctrl + K + A: 从光标处选择到标记点
+ Ctrl + K + W: 从光标处删除到标记点
+ Ctrl + K + X: 交换光标位置和标记位置
+ Ctrl + K + G: 清除标记
+ Ctrl + K + Y: 复制从标记点和光标位置的内容到光标之后
+ Ctrl + Shift + [: 选中代码，按下快捷键，折叠代码
+ Ctrl + Shift + ]: 选中代码，按下快捷键，展开代码
+ Ctrl + K + J: 取消所有折叠代码
+ Ctrl + K + 1: 折叠所有代码
+ Ctrl + K + 2: 折叠第二层次代码
+ Ctrl + K + 3: 折叠第三层次代码
+ Ctrl + K + 4: 折叠第四层次代码
+ Ctrl + K + 5: 折叠第无层次代码
+ Ctrl + K + 6: 折叠第六层次代码
+ Ctrl + K + 7: 折叠第七层次代码
+ Ctrl + K + 8: 折叠第八层次代码
+ Ctrl + K + 9: 折叠第九层次代码
+ Ctrl + K + T: 折叠属性相关代码
+ Ctrl + K + U: 转换大写
+ Ctrl + K + L: 转换小写
+ Alt + Q: 折行
+ Ctrl + Space: 自动完成，针对中文Windows不起作用（打开输入法）
+ F9: 行排序，按数字、字母、文字排序
+ Ctrl + F9: 大小写敏感进行排序，按数字、字母、文字排序

## 选择(Selecting)
+ Ctrl + Shift + L: 先选中多行，再按下快捷键，会在每行行尾插入光标，即可同时编辑这些行
- ESC: Single Seletion(未知)
+ Ctrl + A: 全选
+ Ctrl + Shift + A: 持续按持续扩大选择区域
+ Ctrl + L: 选中整行，继续操作则继续选择下一行，效果和Shift + ↓效果一样
+ Ctrl + D: 选择当前光标所在的词并高亮该词所有出现的位置，再次 Ctrl + D 选择该词出现的下一个位置，在多重选词的过程中:
- Ctrl + K: 进行跳过
- Ctrl + U: 进行回退
- Esc: 退出多重编辑
+ Ctrl + Shift + Space: 快速选择当前作用域(Scope)的内容，持续按键会逐步扩大选择区域(无作用)
+ Ctrl + Shift + M: 选中括号内的内容，持续按键会逐步扩大选择区域
+ Ctrl + Alt + ↑: 向上添加多行光标，可同时编辑多行
+ Ctrl + Alt + ↓: 向下添加多行光标，可同时编辑多行
+ Ctrl + J + ↑: (未研究)
+ Ctrl + J + ←: (未研究)
+ Ctrl + J + →: (未研究)
+ Ctrl + J, Ctrl + Shift + ←: (未研究)
+ Ctrl + J, Ctrl + Shift + →: (未研究)
+ Ctrl + J, Ctrl + Pageup: (未研究)
+ Ctrl + J, Ctrl + Pagedown: (未研究)

## 查找&替换(Finding&Replacing)
+ Ctrl + F: 进行标准查找，之后:
- Alt + C: 切换大小写敏感(Case- sensitive)模式
- Alt + W: 切换整字匹配(Wholematching)模式
- Alt + R: 切换正则匹配(Regexmatching)模式
+ F3: 跳至当前关键字下一个位置（Enter）
+ Shift + F3: 跳到当前关键字上一个位置（Shift + Enter）
+ Ctrl + I: 显示增量查询面板，持续按键会选择下一个查找结果，Enter结束后，光标会选中结果，可直接编辑
+ Ctrl + H: 进行标准替换
+ Ctrl + Shift + H: 替换下一个关键字
+ Ctrl + F3: 快速查找光标处（或所选内容）的内容
+ Alt + F3: 选中文本按下快捷键，即可一次性选择全部的相同文本进行同时编辑
+ Ctrl + D: 查找所选，每按一次增加一个
+ Ctrl + K + D: 查找所选，每按一次跳过一个
+ Ctrl + E: 用所选去查找(无效)
+ Ctrl + Shift + E: 用所选去替换(无效)
+ Ctrl + Shift + F: 在文件夹内查找(注意，如果不起作用，是因为和输入法的快捷键冲突)
+ F4: 上一个结果
+ Shift + F4: 下一个结果

## 视图(View)
+ Ctrl + K + B: 开启/关闭侧边栏
+ Ctrl + \`: 开启/关闭控制台
+ F11: 切换普通全屏
+ Shift + F11: 切换无干扰全屏
+ Alt + Shift + 1: 窗口分屏，恢复默认1屏(非小键盘的数字)
+ Alt + Shift + 2: 左右分屏2列
+ Alt + Shift + 3: 左右分屏3列
+ Alt + Shift + 4: 左右分屏4列
+ Alt + Shift + 8: 垂直分屏2屏
+ Alt + Shift + 9: 垂直分屏3屏
+ Alt + Shift + 5: 等分4屏
+ Ctrl + K + ↑: 移动文件到新建组窗口
+ Ctrl + K + ↓: 关闭组窗口
+ Ctrl + K， Ctrl + Shift + ↑: 新建组窗口
+ Ctrl + K + ←: 聚焦左组窗口
+ Ctrl + K + →: 聚焦右组窗口
+ Ctrl + 1: 聚焦第一个组窗口
+ Ctrl + 2: 聚焦第二个组窗口
+ Ctrl + K，Ctrl + Shift + ←: 移动文件到左组窗口
+ Ctrl + K，Ctrl + Shift + →: 移动文件到右组窗口
+ F6: 打开/关闭拼写检查
+ Ctrl + F6: 下一个拼写错误
+ Ctrl + Shift + F6: 上一个拼写错误

## 跳转(Goto)
+ Ctrl + P: 跳转到任何位置，↑↓选择条目，按Enter打开本条目，按→打开本条目并保持窗口打开状态，ESC关闭本窗口
- 1、输入当前项目中的文件名，快速搜索文件
- 2、输入@和关键字，查找文件中函数名(同Ctrl + R)
- 3、输入:和数字，跳转到文件中指定行(同Ctrl + G)
- 4、输入#和关键字，查找变量名(同Ctrl + :)
+ Ctrl + R: 打开搜索框，自动带@，输入关键字，查找文件中的函数名
+ Ctrl + Shift + R: 在定义好的项目中跳转到Symbol（无作用）
+ F12: 跳转到符号预定义
+ Shift + F12: 跳转到参考
+ Ctrl + G: 打开搜索框，自动带: ，输入数字跳转到该行代码
+ Ctrl + .: 跳转到上一修改处(快捷键无效，菜单项可用)
+ Ctrl + ,: 跳转到上一修改处(已修改为通过插件的行自动完成)(4107已经去掉)
+ Alt + -: 跳回
+ Alt + Shift + -: 前进
+ Ctrl + PageDown: 向左切换当前窗口的标签页
+ Ctrl + PageUp: 向右切换当前窗口的标签页
+ Ctrl + Tab: 定义堆栈中的下一个视图，此快捷键会按照打开顺序相反的方向打开视图
+ Ctrl + Shift + Tab: 定义堆栈中的上一个视图
+ Alt + O: 交换头文件和实现文件
+ Alt + 1: 切换第一个标签文件
+ Alt + 2: 切换第二个标签文件
+ Ctrl + K + C: 将光标所在位置定位到屏幕中央
+ Ctrl + ↑: 向下滚动一行，移动当前显示区域
+ Ctrl + ↓: 向上滚动一行，移动当前显示区域
+ Ctrl + F2: 书签开关
+ F2: 下一个书签
+ Shift + F2: 上一个书签
+ Ctrl + Shift + F2: 清除所有书签
+ Alt + F2: 选择所有书签，此时出现多光标，可以编辑
+ Ctrl + M: 光标移动至括号内结束或开始的位置

## 工具(Tools)
+ Ctrl + Shift + P: 调出命令板(CommandPalette)
+ Ctrl + B: 构建并运行（F7）
+ Ctrl + Shift + B: 用...构建并运行
+ Ctrl + Break: 取消构建
+ Shift + ESC: 查看构建结果
+ F4: 下个构建结果
+ Shift + F4: 上个构建结果
+ Ctrl + Q: 切换录制宏(开始/结束)
+ Ctrl + Shift + Q: 运行宏
+ Ctrl + Alt + Shift + P: 显示文件Scope名称

## 工程(Project)
+ 无快捷键

## 参考(Preference)
+ Ctrl + =: 放大字体
+ Ctrl + Shift + =: 缩小字体（Ctrl + -）

## 帮助(Help)
+ 无快捷键

## 其他(Others)
- ↑↓←→: 上下左右移动光标
- Ctrl + ←/→: 进行逐词左右移动（Alt + ←/→效果同上）
- Alt: 调出菜单- Shift + Tab: 向左缩进(光标在行首)
- Ctrl + Shift + I: 显示增量查询面板，持续按键会选择上一个查找结果，Enter结束后，光标会选中结果，可以直接编辑，提交编码速度
+ Ctrl + J: ?
- Tab: 向右缩进
- Shift + ←: 向左选中文本
- Shift + →: 向右选中文本
- Ctrl + Shift + ←: 向左单位性地选中文本
- Ctrl + Shift + →: 向右单位性地选中文本
- Ctrl + Alt + Enter: 替换所有关键字匹配
- Ctrl + :: 打开搜索框，自动带#，输入关键字，查找文件中的变量名、属性名等
- Esc: 退出光标多行选择，退出搜索框，命令框等
+ Ctrl + 0: 将焦点移到侧边栏，移到侧边栏之后，可以用键盘上下键选中文件
- Ctrl + F2: 设置书签
- Ctrl + Shift + Z: 反撤销还原撤销之后的内容
- Shift + Delete: 删除整行
- Ctrl + Shift + Delete: 删除到行尾
- Ctrl + Shift + Backspace: 删除到行首
- Ctrl + Shift + Number: 分屏之后，使用Ctrl + 数字键跳转到指定屏，使用Ctrl + Shift + 数字键将当前屏移动到指定屏
- Ctrl + Home: 跳转到第一行第一列
- Ctrl + End: 跳转到最后一行最后一列
- 在不同的文件类型中，当选中内容按单引号、双引号、括号、星号等后，则用此符号包围所选内容
- 在控制台输入: sublime.log_commands(True)，可以查看所有动作的日志

## 定制
- Ctrl + Alt + D: 插入当前日期，格式为: 2020-01-01
- Ctrl + Alt + T: 插入当前时间，格式为: 11:11:26
- Ctrl + Alt + A: 插入当前时间和式日期，格式为: 2022-02-22 10:58:56
- Ctrl + Alt + H: 打开此帮助文件
- Ctrl + Alt + N: 打开笔记文件
- Ctrl + , : 完成行
- Alt + ' : 删除重复的行
- Alt + L: 光标向右移动
- Alt + J: 光标向左移动
- Alt + I: 光标向上移动
- Alt + K: 光标向下移动
- Alt + H: 光标移动到行首
- Alt + ;: 光标移动到行尾
- Alt + Ctrl + L: 光标按字右移
- Alt + Ctrl + J: 光标按字左移
- Alt + Shift + I: 光标右移并选择
- Alt + Shift + J: 光标左移并选择
- Alt + Shift + I: 光标上移并选择
- Alt + Shift + K: 光标下移并选择
- Alt + Shift + H: 光标移动到行首并选择
- Alt + Shift + ;: 光标移动到行尾并选择
