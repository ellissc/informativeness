library (tidyverse)
library(forcats)

df = read_csv("./r-data_12-2.csv")

hist(df$prop1,xlab="proportion of target verb",main="Histogram of target verb proportions")
plot(df$prop2,df$prop1,xlab="Proportion of 2nd highest frequent verb",ylab="Proportion of target verb",main="Overall guess proportion distribution")
abline(v=0.66)
abline(h=0.66)
abline(v=0.33)
abline(h=0.33)


ggplot(df, aes(x=prop2, y = prop1))+
  geom_point()+
  facet_wrap(~verb1)+
  theme_bw()

verbs= unique(df$verb1)
for (i in verbs){
  df_temp <- filter(df,verb1 ==i)
  print(length(unique(df_temp$verb2)))
}
#70 max colors
for (i in verbs){
  df_temp <- filter(df,verb1 ==i)
  unique(df_temp$verb2)
  plot(df_temp$prop2,df_temp$prop1,xlim=c(0,1),ylim=c(0,1),xlab="Proportion of 2nd highest frequent verb",ylab="Proportion of target verb",main=paste(i,"guess proportion distribution"),pch=15,col=rainbow(70)[match(df_temp$verb2,unique(df_temp$verb2))])
  legend("topright",legend=unique(df_temp$verb2),pch=15,col=rainbow(length(unique(df_temp$verb2)))[match(df_temp$verb2,unique(df_temp$verb2))])
  abline(v=0.66)
  abline(h=0.66)
  abline(v=0.33)
  abline(h=0.33)
}

for (i in verbs){
  df_temp <- filter(df,verb1 ==i)
  unique(df_temp$verb2)
  plot(df_temp$prop2,df_temp$prop1,type="n",xlim=c(0,1),ylim=c(0,1),xlab="Proportion of 2nd highest frequent verb",ylab="Proportion of target verb",main=paste(i,"guess proportion distribution"))
  text(df_temp$prop2,df_temp$prop1,labels=df_temp$verb2)
  abline(v=0.66)
  abline(h=0.66)
  abline(v=0.33)
  abline(h=0.33)
}

for (i in verbs){
  png(file=paste("./graphs/",i,"_guess_distr.png"),width=820, height=650)
  df_temp <- filter(df,verb1 ==i)
  plot(df_temp$prop2,df_temp$prop1,xlim=c(0,1),ylim=c(0,1),xlab="Proportion of 2nd highest frequent verb",ylab="Proportion of target verb",main=paste(i,"guess proportion distribution"))
  abline(v=0.66)
  abline(h=0.66)
  abline(v=0.33)
  abline(h=0.33)
  dev.off()
}



targets = unique(rand$target)
for (i in targets) {
  temp_plot = ggplot(subset(rand,target==i),aes(x=lemma))+
    geom_bar(stat="count")+
    theme(axis.text.x = element_text(angle = 45))+
    ggtitle("verb",i)
  ggsave(temp_plot, file=paste0("plot_",i,"_8-5.png"), width = 14, height = 10, units = "cm")
  
}