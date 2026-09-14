library(GA);f<-function(x)-sum(x^2);g<-ga(type='real-valued',fitness=f,lower=rep(-5,5),upper=rep(5,5),popSize=40,maxiter=100);print(g@solution)
