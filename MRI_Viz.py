def PlotNiftiTest(Image:numpy.ndarray,X,Y,Z):
	print ('im here')


def PlotNiftiXYZ(Image:numpy.ndarray,X,Y,Z):
  '''
  Plot the 3D axial cuts
  Image - 3D Gray image in a 3D Array
  X - Left .. Right
  Y - Rear .. Front
  Z - Down .. Up
  '''
  maxX,maxY,maxZ = Image.shape

  axz=plt.subplot(2,2,1)
  axz.set_title('Z='+str(Z))
  plt.imshow(Image[:,:,Z], cmap = 'gray')
  plt.plot([0,5],[X,X],color='r')
  plt.plot([Y,Y],[maxX-5-1,maxX-1],color='y')
  #plt.xticks([])
  #plt.yticks([])
  plt.xlabel('Y')
  plt.ylabel('X')
  plt.gcf().set_size_inches(8,8)

  axy=plt.subplot(2,2,2)
  axy.set_title('Y='+str(Y))
  plt.imshow(Image[:,Y,:], cmap = 'gray')
  plt.plot([0,5],[X,X],color='r')
  plt.plot([Z,Z],[maxX-5-1,maxX-1],color='g')
  #plt.xticks([])
  #plt.yticks([])
  plt.xlabel('Z')
  plt.ylabel('X')
  plt.gcf().set_size_inches(8,8)

  axx=plt.subplot(2,2,3)
  axx.set_title('X='+str(X))
  plt.imshow(Image[X,:,:], cmap = 'gray')
  plt.plot([0,5],[Y,Y],color='y')
  plt.plot([Z,Z],[maxY-5-1,maxY-1],color='g')
  #plt.xticks([])
  #plt.yticks([])
  plt.xlabel('Z')
  plt.ylabel('Y')
  plt.gcf().set_size_inches(8,8)
  #plt.legend()
  plt.show()

def PlotNifti(Image,Axis,Start,N = 25):
  '''
  Print N cuts in an axis
  Image - 3D Gray image in a 3D Array
  Axis - X, Y or Z
  Start - Start cut number
  N - Number of cuts
  '''
  maxChartLines = N//5 +1

  maxX,maxY,maxZ = Image.shape

  if Axis == "x" or Axis=="X":
    if Start+N < maxX:
      Xmax = Start + N
    else:
      Xmax=maxX
    for i in range(Start, Xmax):
      ax=plt.subplot(5,maxChartLines ,i+1-Start)
      ax.set_title('X='+str(i))
      plt.imshow(Image[i,:,:], cmap = 'gray')
      plt.gcf().set_size_inches(15,15)
      plt.xticks([])
      plt.yticks([])
    plt.show()
  elif Axis == "y" or Axis=="Y":
    if Start+N < maxY:
      Ymax = Start + N
    else:
      Ymax=maxY
    for i in range(Start,Ymax):
      ay=plt.subplot(5,maxChartLines ,i+1-Start)
      ay.set_title('Y='+str(i))
      plt.imshow(Image[:,i,:], cmap = 'gray')
      plt.gcf().set_size_inches(15,15)
      plt.xticks([])
      plt.yticks([])
    plt.show()
  elif Axis == "z" or Axis=="Z":
    if Start+N < maxZ:
      Zmax = Start + N
    else:
      Zmax=maxZ
    for i in range(Start,Zmax):
      az=plt.subplot(5,maxChartLines ,i+1-Start)
      az.set_title('Z='+str(i))
      plt.imshow(Image[:,:,i], cmap = 'gray')
      plt.gcf().set_size_inches(15,15)
      plt.xticks([])
      plt.yticks([])
    plt.show()
  else:
    print('Axis must be X,Y or Z')