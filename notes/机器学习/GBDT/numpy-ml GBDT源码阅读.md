[CSDN](https://blog.csdn.net/TQCAI666/article/details/113246321)

交叉熵的公式是$-\Sigma_k^{K}p(y_k)\log p(\hat{y}_k)$，

对 $\hat{y}$ 求导后得到 $-\Sigma_k^{K}\frac{p(y_k)}{ p(\hat{y}_k)}$

体现在这个公式中：

`numpy_ml.trees.losses.CrossEntropyLoss.grad`

```python
def grad(self, y, y_pred):
    eps = np.finfo(float).eps   # 对y_pred求导
    return -y * 1 / (y_pred + eps)
```

注意到，对于分类任务，如果有$K$个类，本质上是训练$K$个树，然后用OHE将类别$y \in [0,K)$处理为k个0,1的列向量。所以对于第k个分量，交叉熵退化为 $-p(y)\log p(\hat{y})$ 。

每步决策树拟合的负梯度：$\frac{p(y)}{ p(\hat{y})}$

||$y=0$|$y=1$|
|--|--|--|
|$\hat{y}=0$|0|$\infin$|
|$\hat{y}=1$|0|1|
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210127131020987.png)


