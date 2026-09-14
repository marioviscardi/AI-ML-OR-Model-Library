library(glmnet)
set.seed(42);x<-matrix(rnorm(1000),ncol=10);y<-2*x[,1]-x[,2]+rnorm(nrow(x));print(glmnet(x,y,alpha=0));print(glmnet(x,y,alpha=1));print(glmnet(x,y,alpha=.5))
