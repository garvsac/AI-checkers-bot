#Garv Sachdeva
#2015B4A7055P

from xd import *

MaxUtility = 1e9

MAX_DEPTH = 3
def minimax(depth , curBoard , minimaxnodes ):
  minimaxnodes = minimaxnodes + 1
  def maxValue(board, depth):
    val = -MaxUtility
    #print 'maxval'
    for successor in Successor_function(board,2):
      val = max(val, minimax(depth+1,successor,minimaxnodes))
    return val
  def minValue(board, depth):
    val = MaxUtility
    #print 'minval'
    for successor in Successor_function(board,1):
      val = min(val, minimax(depth+1,successor,minimaxnodes))
    return val

  if ( Terminal_test(curBoard)):
  	return eval_teminal(curBoard)
  if (depth >= MAX_DEPTH):
    return eval(curBoard)
  if(depth%2==0):
    return maxValue(curBoard, depth)
  else:
    return minValue(curBoard, depth)


def minimaxhead(board):
  minimaxnodes=0
  val = -MaxUtility
  nextmove = Successor_function(board,2)[0]
  for successor in Successor_function(board,2):
    temp = minimax(1,successor,minimaxnodes)
    if( temp > val):
      val = temp
      nextmove = successor
  return nextmove


