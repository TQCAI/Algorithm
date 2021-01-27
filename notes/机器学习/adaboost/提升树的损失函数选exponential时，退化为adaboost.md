[CSDN](https://blog.csdn.net/TQCAI666/article/details/113240075)

结论：提升树的损失函数选`指数损失函数`时，退化为`adaboost`

证明见《统计学习方法-第一版》 p145-146
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210127092620864.png)
[scikit-learn 梯度提升树(GBDT)调参小结](https://www.cnblogs.com/pinard/p/6143927.html)

>对于分类模型，有**对数似然损失函数"deviance"**和**指数损失函数"exponential"**两者输入选择。默认是对数似然损失函数"deviance"。在原理篇中对这些分类损失函数有详细的介绍。一般来说，推荐使用默认的"deviance"。它对二元~~分离~~分类 和多元分类各自都有比较好的优化。==而指数损失函数等于把我们带到了Adaboost算法==。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210127093401802.png#pic_center)
[梯度提升树(GBDT)原理小结](https://www.cnblogs.com/pinard/p/6140514.html)


![在这里插入图片描述](https://img-blog.csdnimg.cn/20210127094315930.png)

![在这里插入图片描述](https://img-blog.csdnimg.cn/2021012709551895.png)![在这里插入图片描述](https://img-blog.csdnimg.cn/20210127095539221.png)


