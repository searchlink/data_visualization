# 结合django和echarts搭建数据分析平台  

数据和案例来自[How to Use Chart.js with Django](https://simpleisbetterthancomplex.com/tutorial/2020/01/19/how-to-use-chart-js-with-django.html), 很感谢提供的场景和思路。

1. 尝试了从mysql查询数据，进行echarts前端展示，绘制了关于城市人口数top5的饼图，效果如下：     
![城市人口分布top5](https://github.com/searchlink/data_visualization/blob/master/statics/images/%E5%9F%8E%E5%B8%82%E4%BA%BA%E5%8F%A3top5.png)

2. 通过异步加载从mysql查询数据，进行echarts前端展示，绘制了国家-人口分布的柱状图，效果如下：   
![国家人口分布](https://github.com/searchlink/data_visualization/blob/master/statics/images/%E5%9B%BD%E5%AE%B6%E4%BA%BA%E5%8F%A3%E5%88%86%E5%B8%83.png)        

接下来会继续完善整个项目，欢迎关注~