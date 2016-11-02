---
title: Really Big Data: Analytics on Graphs with Trillions of Edges 
date: 2016-10-13 18:46:52
update: 2016-10-13 18:46:52
---
Really Big Data: Analytics on Graphs with Trillions of Edges 

Willy zwaenepoel 

School of Computer and Communication Sciences 

EPFL  瑞士联邦理工学院洛桑/ 洛桑联邦理工学院，是瑞士的两所联邦理工学院之一，成立
于1853年，其姊妹校苏黎世联邦理工学院则位于德语区。2012在校生约9300名，其中包括
4,800多名本科生和4,200多名研究生。

Big graphs occur naturally in many applications, most obviously in social networks,but also in many other areas such as biology and forensics. Current approaches to processing large graphs use either supercomputers or very large clusters. In both cases the entire graph must reside in memory before it can be processed. We are pursuing an alternative approach, processing graphs from secondary storage. While this comes with a performance penalty, it makes analytics on very large graphs feasible on a small number of commodity machines. We have developed two systems, one for a single machine and one for a cluster of machines. X-Stream, the single machine solution, aims to make all secondary storage access sequential. It uses two techniques to achieve this goal, edge-centric processing and streaming partitions. Chaos, the cluster solution, starts from the observation that there is little benefit to locality when accessing data from secondary storage over a high-speed network. As a result, Chaos spreads graph data uniformly randomly over storage devices, and uses randomized access to achieve I/O balance. Chaos furthermore uses work stealing to achieve computational load balance. By using these techniques, it avoids the need for expensive partitioning during pre-processing, while still achieving good scaling behavior. With Chaos we have been able to process an 8-trillion-edge graph on 32 machines, a new milestone for graph size on a small cluster. I will describe both systems and their performance on a number of benchmarks and in comparison to state-of-the-art alternatives. 

Prof. Dr. Willy Zwaenepoel received his BS/MS from the University of Gent, Belgium, and his 
PhD from Stanford University. He is currently a Professor of Computer Science at EPFL. Before he 
has held appointments as Professor of Computer Science and Electrical Engineering at Rice 
University, and as Dean of the School of Computer and Communication Sciences at EPFL. His 
interests are in operating systems and distributed systems. He is a Fellow of the ACM and the 
IEEE, he has received the IEEE Kanai Award and several best paper awards, and is a member of 
the Belgian and European Academies. He is most well known for his work on the Treadmarks 
distributed shared memory system, which was licensed to Intel and became the basis for Intel's 
OpenMP cluster product. He has also been involved in a number of startups, including BugBuster 
(acquired by AppDynamics), iMimic (acquired by Ironport/ Cisco) , Midokura and Nutanix. 

