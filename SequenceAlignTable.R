##Code of printing out the dynamic programming table for sequence alignment 


#################################global alignment##########################################
pdf("hw2_global.pdf")
plot(1,1,type = "n", ann = F, axes = F, xlim = c(0,11), ylim = c(0,11))
for (i in 0:11)
	abline(h = i)
for (i in 0:11)
	abline(v = i)
v <- c('T','A','C','G','G','G','T','A','T')
w <- c('G','G','A','C','G','T','A','C','G')
text(1.5, 9.5, 0, cex = 0.8, font =2)
L_Label <- function(){
	y = 10.5
	x = 2.5
	for (t in v)
	{
		text(x,y,t,cex = 0.8, font = 2)
		text(x,y-1,-x+1.5, cex = 0.8, font = 2)
		x = x+1
	}
	x = 0.5
	y = 8.5
	for (t in w)
	{
		text(x,y,t,cex = 0.8, font = 2)
		text(x+1,y,y-9.5, cex = 0.8, font = 2)
		y= y-1
	}
}
L_Label()


res <- matrix(nrow = 10, ncol = 10)
for (i in 1:10)
{
	res[1,i] <- -i+1
	res[i,1] <- -i+1
}
numbers <- function(){
	for (j in 1:9)
		for (i in 1:9)
		{
			up <- res[j,i+1] -1
			left <- res[j+1,i] -1
			angle <- res[j,i]
			if (v[i] == w[j])
				angle = angle +1
			else
				angle = angle -1
			values = c(up,left,angle)
			print(values)
			max <- values[which.max(values)]
			res[j+1,i+1] = max
			text(i+1.5,9.5-j,max,font = 2)
			if (angle == max)
				arrows(i+0.8,10.2-j,i+1.2,9.8-j, length = 0.05, col = 'red', lwd = 2)
			if (left == max)
				arrows(i+0.8,9.5-j,i+1.2,9.5-j, length = 0.05, col = 'blue', lwd = 2)
			if (up == max)
				arrows(i+1.5,10.2-j,i+1.5,9.8-j, length = 0.05, col = 'green', lwd = 2)
		}
}
numbers()
dev.off()


###########################local alignment##################################################
pdf("hw2_local.pdf")
plot(1,1,type = "n", ann = F, axes = F, xlim = c(0,11), ylim = c(0,11))
for (i in 0:11)
	abline(h = i)
for (i in 0:11)
	abline(v = i)
v <- c('T','A','C','G','G','G','T','A','T')
w <- c('G','G','A','C','G','T','A','C','G')
L_Label <- function(){
	y = 10.5
	x = 2.5
	for (t in v)
	{
		text(x,y,t,cex = 0.8, font = 2)
		text(x,y-1,'0', cex = 0.8, font = 2)
		x = x+1
	}
	x = 0.5
	y = 8.5
	for (t in w)
	{
		text(x,y,t,cex = 0.8, font = 2)
		text(x+1,y,'0', cex = 0.8, font = 2)
		y= y-1
	}
}
L_Label()
text(1.5, 9.5, '0', cex = 0.8)

res <- matrix(nrow = 10, ncol = 10)
for (i in 1:10)
{
	res[1,i] <- 0
	res[i,1] <- 0
}
numbers <- function(){
	for (j in 1:9)
		for (i in 1:9)
		{
			up <- res[j,i+1] -1
			left <- res[j+1,i] -1
			angle <- res[j,i]
			if (v[i] == w[j])
				angle = angle +1
			else
				angle = angle -1
			values = c(0,up,left,angle)
			max <- values[which.max(values)]
			res[j+1,i+1] = max
			text(i+1.5,9.5-j,max,font = 2)
			if (angle == max)
				arrows(i+0.7,10.3-j,i+1.3,9.7-j, length = 0.05, col = 'red', lwd = 2)
			if (left == max)
				arrows(i+0.7,9.5-j,i+1.3,9.5-j, length = 0.05, col = 'blue', lwd = 2)
			if (up == max)
				arrows(i+1.5,10.3-j,i+1.5,9.7-j, length = 0.05, col = 'green', lwd = 2)
		}
}
numbers()
dev.off()


###########################affine gap penalty##################################################

pdf("hw2_affine.pdf")
plot(1,1,type = "n", ann = F, axes = F, xlim = c(0,11), ylim = c(0,11))
for (i in 0:11)
	abline(h = i)
for (i in 0:11)
	abline(v = i)
v <- c('T','A','C','G','G','G','T','A','T')
w <- c('G','G','A','C','G','T','A','C','G')
L_Label <- function(){
	y = 10.5
	x = 2.5
	for (t in v)
	{
		text(x,y,t,cex = 0.8, font = 2)
##		text(x,y-1,'0', cex = 0.8, font = 2)
		x = x+1
	}
	x = 0.5
	y = 8.5
	for (t in w)
	{
		text(x,y,t,cex = 0.8, font = 2)
##		text(x+1,y,'0', cex = 0.8, font = 2)
		y= y-1
	}
}
L_Label()
##text(1.5, 9.5, '0', cex = 0.8)

resL <- matrix(nrow = 10, ncol = 10)
resU <- matrix(nrow = 10, ncol = 10)
resA <- matrix(nrow = 10, ncol = 10)
for (i in 1:10)
{
	resL[1,i] <- -0.5*i+0.5
	resU[1,i] = 0.0
	resU[i,1] <- -0.5*i+0.5
	resL[i,1] = 0.0
	resA[1,1] = 0.0
	resA[1,i] = resL[1,i]
	resA[i,1] = resU[i,1]
}
mmax <- function(x, y){
	
}
numbers <- function(){
	for (j in 1:9)
		for (i in 1:9)
		{
			up <- res[j,i+1] -1
			left <- res[j+1,i] -1
			angle <- res[j,i]
			if (v[i] == w[j])
				angle = angle +1
			else
				angle = angle -1
			values = c(0,up,left,angle)
			max <- values[which.max(values)]
			res[j+1,i+1] = max
			text(i+1.5,9.5-j,max,font = 2)
			if (angle == max)
				arrows(i+0.7,10.3-j,i+1.3,9.7-j, length = 0.05, col = 'red', lwd = 2)
			if (left == max)
				arrows(i+0.7,9.5-j,i+1.3,9.5-j, length = 0.05, col = 'blue', lwd = 2)
			if (up == max)
				arrows(i+1.5,10.3-j,i+1.5,9.7-j, length = 0.05, col = 'green', lwd = 2)
		}
}
numbers()
dev.off()




