#Garv Sachdeva
#2015B4A7055P

from xd import *

MaxUtility = 1e9

MAX_DEPTH = 5
def minimax_prun(depth , curBoard , alpha, beta):

  def maxValue(board, depth , alpha, beta):
    val = -MaxUtility
    #print 'maxval'
    for successor in Successor_function(board,2):
      val = max(val, minimax_prun(depth+1,successor , alpha, beta))
      if val >= beta: return val
      alpha = max(alpha, val)
    return val
  def minValue(board, depth , alpha, beta):
    val = MaxUtility
    #print 'minval'
    for successor in Successor_function(board,1):
      val = min(val, minimax_prun(depth+1,successor , alpha, beta))
      if val <= alpha: return val
      beta = min(beta, val)
    return val

  if ( Terminal_test(curBoard)):
  	return eval_teminal(curBoard)
  if (depth >= MAX_DEPTH):
    return eval(curBoard)
  if(depth%2==0):
    return maxValue(curBoard, depth ,alpha, beta)
  else:
    return minValue(curBoard, depth ,alpha, beta)


def minimax_prun_head(board):
  val = -MaxUtility
  nextmove = Successor_function(board,2)[0]
  for successor in Successor_function(board,2):
    temp = minimax_prun(1,successor , -MaxUtility, MaxUtility)
    if( temp > val):
      val = temp
      nextmove = successor
  return nextmove


