# QSBlue

为浙江大学的用户设计的中文 [Typst Touying](https://touying-typ.github.io/zh/) 模板，改编自官方提供的 [University](https://touying-typ.github.io/zh/docs/themes/university) 模板，在此基础上加入了一些个人频繁使用的特性。包括：

- 求是蓝风格配色
- 更简单的页眉标题展示
    - 取消展示一级标题的单独页
    - 页眉可以只展示一级标题，如果有二级标题也一并展示
    - 根据二级标题分页
    - 三级及以上标题显示在正文中
- 经过优化的校徽展示
- 调整页面布局，优化字体大小比例
- grid辅助排版等高级功能的演示

在此之外，模板中删除了一些不常用的功能，方便初学者改进。

## 使用方法

- 在`main.typ`基础上修改即可。
- 如需将`typ`文件转化为PDF文件，请参考[Typst的GitHub页面](https://github.com/typst/typst)，或者使用[官方在线编译平台](https://typst.app/)。
- 如需将`typ`文件转化为PPTX文件，可以参考本项目的`to_pptx.py`脚本。

可以到`example`目录下查看使用本模板生成的PDF与PPTX文件的效果。
