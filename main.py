import discord
import os
import random

client = discord.Client()

@client.event
async def on_ready():
  print('We have loggin in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
      return
    if message.content.startswith("!help"):
      await message.channel.send('GameBot allows you to play MineSweeper and TicTacToe! Try !minehelp and !tictachelp for more information.')
    if message.content.startswith("!minesweep"):
      await message.channel.send(minesweep(10, 10))
    if message.content.startswith("!mineeasy"):
      await message.channel.send(minesweep(8, 5))
    if message.content.startswith("!minehard"):
      await message.channel.send(minesweep(12, 20))
 
    tarr = [[0 for i in range(3)] for j in range(3)]
    if message.content.startswith("!tictactoe"):
      tarr[0][0] = ':one:'
      tarr[0][1] = ':two:'
      tarr[0][2] = ':three:'
      tarr[1][0] = ':four:'
      tarr[1][1] = ':five:'
      tarr[1][2] = ':six:'
      tarr[2][0] = ':seven:'
      tarr[2][1] = ':eight:'
      tarr[2][2] = ':nine:'
      await message.channel.send(tprint(tarr))
    if message.content.startswith("!play 1x"):
      tarr[0][0] = ':boom:'
      await message.channel.send(tprint(tarr))

def minesweep(size, mines):
  arr = [[0 for i in range(size)] for j in range(size)]
  minestring = ''
  count = 0
  while count < mines:
    r = random.randint(0, size-1)
    c = random.randint(0, size-1)
    if arr[r][c] == 0: 
      arr[r][c] = -1
      count += 1
  for i in range(size):
    for j in range(size):
      if arr[i][j] == -1:
        minestring = minestring + ':boom:'
      if arr[i][j] == 0:
        count = 0
        if i!=0 and j!=0 and arr[i-1][j-1] == -1: count = count + 1
        if i!=0 and arr[i-1][j] == -1: count = count + 1
        if i!=0 and j!=size-1 and arr[i-1][j+1] == -1: count = count + 1
        if j!=0 and arr[i][j-1] == -1: count = count + 1
        if j!=size-1 and arr[i][j+1] == -1: count = count + 1
        if i!=size-1 and j!=0 and arr[i+1][j-1] == -1: count = count + 1
        if i!=size-1 and arr[i+1][j] == -1: count = count + 1
        if i!=size-1 and j!=size-1 and arr[i+1][j+1] == -1: count = count + 1
        if count == 0: minestring += ':zero:'
        if count == 1: minestring += ':one:'
        if count == 2: minestring += ':two:'
        if count == 3: minestring += ':three:'
        if count == 4: minestring += ':four:'
        if count == 5: minestring += ':five:'
        if count == 6: minestring += ':six:'
        if count == 7: minestring += ':seven:'
        if count == 8: minestring += ':eight:'
    minestring += '\n'
  return minestring

def tprint(tarr):
  tttstring = ''
  for i in range(3):
    for j in range(3):
      tttstring += tarr[i][j]
    tttstring += '\n'
  return tttstring

def tupdate(tarr, num, play):
  tttstring = ''
  tarr[0][0] = ':nine:'
  for i in range(3):
    for j in range(3):
      tttstring += tarr[i][j]
    tttstring += '\n'
  return tarr[0][0]


client.run(os.getenv('TOKEN'))