#运用解包语法. h,sum = 100.0,0.0; 是有错误的!

#运用了format()格式化。 .

#陈晓莉

h,sum = 100.0,0.0



for i in range(10):

    h = h/2;

    sum += 2 * h;



print("移动总距离为:{},当前高度为:{}".format(sum+100,h))


