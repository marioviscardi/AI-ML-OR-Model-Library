data(iris);hc<-hclust(dist(scale(iris[,1:4])),method='ward.D2');print(table(cutree(hc,k=3),iris$Species))
