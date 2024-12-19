#case1
from bokeh.plotting import figure,output_file,show
x=[1,2,3,4,5]
y=[2,4,6,8,10]
output_file('line.html')
fig=figure(title='Line plot',x_axis_label='x',y_axis_label='y')
fig.line(x,y)
show(fig)

#case2
from bokeh.plotting import figure,output_file,show
fig=figure(min_width=800,min_height=200)
fig.hbar(y=[2,4,6],height=1,left=0,right=[1,2,3],color='cyan')
output_file('bar.html')
show(fig)

#case3
from bokeh.plotting import figure,output_file,show
fig=figure(min_width=800,min_height=200)
fig.vbar(x=[2,4,6],width=1,bottom=0,top=[10,8,4],color='cyan')
output_file('vbar.html')
show(fig)

#case4
from bokeh.plotting import figure,output_file,show
p=figure(min_width=800,min_height=200)
p.patch(x=[1,3,2,4],y=[2,3,5,7],color='green')
output_file('patch.html')
show(p)

#case5
from bokeh.plotting import figure,output_file,show
p=figure(min_width=800,min_height=400)
p.scatter([1,4,3,2,5],[6,5,2,4,7],marker='circle',size=20,fill_color='green')
output_file('scatter.html')
show(p)

#case6
from bokeh.plotting import figure,output_file,show
p=figure(min_width=800,min_height=400)
x=[1,2,5,7,9]
y1=[2,5,4,6,8]
y2=[5,9,11,12,15]
p.varea(x=x,y1=y1,y2=y2)
output_file('area.html')
show(p)
