# TCN 
An Empirical Evaluation of Generic Convolutional and Recurrent Networks for Sequence Modeling<br>
https://arxiv.org/pdf/1803.01271.pdf

# Architecture
TCN (Temporal Convolution Network) 於2018年提出。由於 RNN 在經過不斷的演進與迭代發展下，產生了像是 LSTM 和 GRU ，都能有效解決時序問題，故在我們的知識中，甚至是一些機器學習的教科書中，已經反射性的把 RNN 列為解決序列問題的工具，但是就在最近的公開論文中提到，作為 CNN 家族的其中一個成員：TCN，在各項資料集中成功的擊敗了當下的王者 RNN 成為新的序列 data 分析方面的橋楮。<br>
![](https://provenclei.github.io/assets/tcn/tcn_11.png)<br>
TCN 的特點:
* 結構上的卷積是因果關係，即沒有從未來到過去的信息洩漏
* 結構可以獲取任意長度的序列，並將其映射到相同長度的輸出序列，就像使用RNN一樣

# TCN Sequence modeling
假設:
* input sequence: x0, x1, x2, …, xT
* output sequence: y0, y1, y2, …, yT
預測T時間的輸出: <br>
![](https://img-blog.csdnimg.cn/20190503170412750.png)
loss function: <br>
![](https://img-blog.csdnimg.cn/20190503170443291.png)

# TCN Causal Convolutions
![](https://img-blog.csdnimg.cn/20190503170519803.png)<br>
TCN 的目標:
* 網路的上一層到下一層，輸入與輸出的長度相同
* 不存在利用將來信息的情形
解決方案:
* Full-Convolutional Network
* casual convolution
![](https://provenclei.github.io/assets/tcn/tcn_11.png)<br>

# TCN Dilated Convolutions
