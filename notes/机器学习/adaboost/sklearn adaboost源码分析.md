[CSDN](https://blog.csdn.net/TQCAI666/article/details/113248906)

`sklearn.ensemble._weight_boosting.BaseWeightBoosting.fit`

```python
for iboost in range(self.n_estimators):
    # Boosting step
    sample_weight, estimator_weight, estimator_error = self._boost(
        iboost,
        X, y,
        sample_weight,
        random_state)

    sample_weight_sum = np.sum(sample_weight)

    if iboost < self.n_estimators - 1:
        # Normalize
        sample_weight /= sample_weight_sum
```

`sklearn.ensemble._weight_boosting.AdaBoostClassifier._boost_discrete`

```python
estimator.fit(X, y, sample_weight=sample_weight)
```

`sample_weight`就是$w_{mi}$，根据样本权重进行拟合

```python
# Instances incorrectly classified
incorrect = y_predict != y

# Error fraction
estimator_error = np.mean(
    np.average(incorrect, weights=sample_weight, axis=0))
```

误分类率是误分类样本权重和： $e_m=\sum_{i=1}^{N}w_{mi}I(G_m(x_i)\neq y_i)$


![在这里插入图片描述](https://img-blog.csdnimg.cn/20210127150641921.png)

如果弱学习器的效果连随机都如不，早停。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210127150803511.png)

计算$G_m$的系数$\alpha_m=\frac{1}{2}log\frac{1-e_m}{e_m}$

`SAMME`算法考虑了多分类，乘以learning_rate的衰减实现正则化。



![在这里插入图片描述](https://img-blog.csdnimg.cn/20210127151220720.png)

$w_{mi}=exp(-y_i \alpha_{m-1} G_{m-1}(x_i))$

试想，$y\times \hat{y}$，二分类时只有二者不同时才为1

这么写其实也兼顾了多分类的情况。对于多分类其实只需要修改$\alpha_m$也就是代码中的`estimator_weight`的计算而已。


