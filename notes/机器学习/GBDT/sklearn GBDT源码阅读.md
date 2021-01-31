[CSDN](https://blog.csdn.net/TQCAI666/article/details/113252587)



- `ls`

```python
class LeastSquaresError(RegressionLossFunction):
    def init_estimator(self):
        return DummyRegressor(strategy='mean')

    def __call__(self, y, raw_predictions, sample_weight=None):
        return (1 / sample_weight.sum() * np.sum(
            sample_weight * ((y - raw_predictions.ravel()) ** 2)))

    def negative_gradient(self, y, raw_predictions, **kargs):
        return y - raw_predictions.ravel()
```

- `lad`

```python
class LeastAbsoluteError(RegressionLossFunction):
    def init_estimator(self):
        return DummyRegressor(strategy='quantile', quantile=.5)

    def __call__(self, y, raw_predictions, sample_weight=None):
        return (1 / sample_weight.sum() * np.sum(
            sample_weight * np.abs(y - raw_predictions.ravel())))

    def negative_gradient(self, y, raw_predictions, **kargs):
        raw_predictions = raw_predictions.ravel()
        return 2 * (y - raw_predictions > 0) - 1
```

- `huber`

```python
class HuberLossFunction(RegressionLossFunction):
    def __init__(self, alpha=0.9):
        super().__init__()
        self.alpha = alpha
        self.gamma = None

    def init_estimator(self):
        return DummyRegressor(strategy='quantile', quantile=.5)

    def __call__(self, y, raw_predictions, sample_weight=None):
        raw_predictions = raw_predictions.ravel()
        diff = y - raw_predictions
        gamma = self.gamma
        if gamma is None:
            if sample_weight is None:
                gamma = np.percentile(np.abs(diff), self.alpha * 100)
            else:
                gamma = _weighted_percentile(np.abs(diff), sample_weight,
                                             self.alpha * 100)

        gamma_mask = np.abs(diff) <= gamma
        sq_loss = np.sum(0.5 * sample_weight[gamma_mask] *
                         diff[gamma_mask] ** 2)
        lin_loss = np.sum(gamma * sample_weight[~gamma_mask] *
                          (np.abs(diff[~gamma_mask]) - gamma / 2))
        loss = (sq_loss + lin_loss) / sample_weight.sum()
        return loss

    def negative_gradient(self, y, raw_predictions, sample_weight=None,
                          **kargs):
        raw_predictions = raw_predictions.ravel()
        diff = y - raw_predictions
        if sample_weight is None:
            gamma = np.percentile(np.abs(diff), self.alpha * 100)
        else:
            gamma = _weighted_percentile(np.abs(diff), sample_weight,
                                         self.alpha * 100)
        gamma_mask = np.abs(diff) <= gamma
        residual = np.zeros((y.shape[0],), dtype=np.float64)
        residual[gamma_mask] = diff[gamma_mask]
        residual[~gamma_mask] = gamma * np.sign(diff[~gamma_mask])
        self.gamma = gamma
        return residual
```

- `quantile`

```python
class QuantileLossFunction(RegressionLossFunction):
    def __init__(self, alpha=0.9):
        super().__init__()
        self.alpha = alpha
        self.percentile = alpha * 100

    def init_estimator(self):
        return DummyRegressor(strategy='quantile', quantile=self.alpha)

    def __call__(self, y, raw_predictions, sample_weight=None):
        raw_predictions = raw_predictions.ravel()
        diff = y - raw_predictions
        alpha = self.alpha

        mask = y > raw_predictions
        if sample_weight is None:
            loss = (alpha * diff[mask].sum() -
                    (1 - alpha) * diff[~mask].sum()) / y.shape[0]
        else:
            loss = ((alpha * np.sum(sample_weight[mask] * diff[mask]) -
                    (1 - alpha) * np.sum(sample_weight[~mask] *
                                         diff[~mask])) / sample_weight.sum())
        return loss

    def negative_gradient(self, y, raw_predictions, **kargs):
        alpha = self.alpha
        raw_predictions = raw_predictions.ravel()
        mask = y > raw_predictions
        return (alpha * mask) - ((1 - alpha) * ~mask)
```

- `deviance`


<img src="https://img-blog.csdnimg.cn/20210127163806387.png" width=300><img>

二项式偏差度

```python
from scipy.special import expit, logsumexp

class BinomialDeviance(ClassificationLossFunction):
    def init_estimator(self):
        return DummyClassifier(strategy='prior')

    def __call__(self, y, raw_predictions, sample_weight=None):
        return (-2 / sample_weight.sum() * np.sum(
            sample_weight * ((y * raw_predictions) -
                             np.logaddexp(0, raw_predictions))))

    def negative_gradient(self, y, raw_predictions, **kargs):
        return y - expit(raw_predictions.ravel())
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210127164318621.png)
这个公式化简一下是 $-2[y\cdot \hat{y}-log(1+e^{\hat{y}})]$


这个损失函数与numpy-ml不同，这篇博客讲的很透彻：

[Scikit Binomial Deviance Loss Function](https://stats.stackexchange.com/questions/157870/scikit-binomial-deviance-loss-function)


推下这个式子的负梯度

$=y-\frac{e^{\hat{y}}}{1+e^{\hat{y}}}=y-\frac{1}{1+e^{-\hat{y}}}=y-\sigma(\hat{y})$


