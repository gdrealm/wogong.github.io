---
title: PSCAN:网络大数据的并行聚类算法
date: 2016-06-20
---

徐晓伟 Xiaowei Xu,University of Arkansas at Little Rock
1983，南开数学系毕业
与苏总同学
慕尼黑 博士

## 摘要
社交网络有着大量的用户，是大数据的主要来源。徐晓伟博士将介绍网络大数据的特征和所面临主要挑战，基于结构的网络聚类算法PSCAN不仅可以发现网络中的社区，而且可以发现一些具有特殊功能的节点包括链接枢纽。SCAN算法已经在多个领域发挥着作用：在生物领域的新陈代谢网络分析、蛋白质相互作用网络分析，对于理解生物系统的组织和功能以及未知蛋白质功能预测具有重要的意义。另外，自“911事件”以来，世界各国试图用包括社区发现在内的的多种社会网络分析手段对恐怖主义活动进行分析，通过发现社会网络、电信网络以及互联网络中的犯罪网络，并迅速馈定犯罪分子的领导者，对其及其团伙的犯罪行为进行全方位的关联跟踪，进而有效引击犯罪网络，维护社会政治经济的稳定。社区发现再互联网上的应用则更为广泛，如在微博中利用社区发现用于精准广告投放，对电子商务中的用户进行社区发现从而帮助其建立更可靠的推荐系统。针对大数据的严重挑战，徐博士及其研究团队开发了基于大数据平台Hadoop/MapReduce的并行算法PSCAN。PSCAN可以有效地处理大数据网络并具有很高的可伸缩性（scalability）和加速比（speedup）。

## Note
### background
1. Social networks are big data:
	- volume
	- velicity
	- variety
2. dataminr.com startup in Wall Street
3. Graphs

### Outline
1. Structure clustering algorithm for network
2. Parallel Algorithm for big network
3. Conclusion

### content
1. Community structure/cluster
2. functional roles of nodes
	* Hub
	* Outliner
	* Leader
3. sociological inspiration
4. Structure similarity measures shared friends == SS
	* $\sigma(v,w)$
	* SCAN: Structural Clustering Algorithm for Networks
	* 2 parameters: $\mu=2$ community 最少成员, $\varepsilon=0.7$ 大于此值算同一个 Comminity
5. Complexity：Linear
6. Determine parameter
	* fix $\mu=2$
	* Run SCAN for $\varepsilon=0.1, 0.2, 0.3, ...$
	* Choose the optimal $\varepsilon$, which maxize Q
7. MapReduce
8. Parallel SCAN algorithm
9. Parallel SCAN algorithm in MapReduce
	1. **step-1: calculate SS**
	2. step-2: cut off edges with $SS<\varepsilon$
	3. step-3: Find all connected components
10. Synthetic datasets
11. Performance measure
	* Speedup
	* Scaleup
12. Conclusion
