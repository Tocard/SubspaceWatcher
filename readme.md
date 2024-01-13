# SubspaceWatcher

This simple python script will log your wallet & staking change over time.

## Warning
Rembember that when you run code that you hvn't wrote, be always carefull of what you're doing.
Even if you write code, be carefull of what you're using.



## how to install & run

```shell
python3 -m venv .
source bin/activate
pip install -r req.txt

python3 main.py --help
```
## Explanation

````shell
Usage: main.py [OPTIONS]

Options:
  -n, --node_rpc TEXT           node rpc url (do not forget to enable cors &
                                rpc external)
  -w, --wallet TEXT             wallet to watch
  -b, --block_interval INTEGER  number of block between occurence (around a
                                day for 13292)
  -o, --occurence INTEGER       number of occurence
  -d, --debug                   Enable debug if specified
  --help                        Show this message and exit.

````

` --node_rpc` should be something like `ws://your_ip:9944`. You will need to run node with this flag to make it work
`--rpc-external --rpc-methods unsafe --unsafe-rpc-external --rpc-cors all` So DO NOT OPEN YOUR NODE on internet :)
If you find a safest way, tell me !

`--wallet` is just the wallet to watch

`--block_interval` is the number of block between call. by default it's around one day

`--occurence` is the number of value to get, by default 10 * `--block_interval` mean 10 days.


## Output
````log
2024-01-13 15:41:19,821 INFO | subspace.watcher | We assume an average block time of 6.5s for time estimation
2024-01-13 15:41:20,422 INFO | subspace.watcher | Start Counting at block 1082557, with 13292 block interval & 10 step at 2024-01-13 14:41:20.422109.
2024-01-13 15:41:20,438 SUCCESS | subspace.watcher | Balance at block 949637 2024-01-03 14:41:40.422109: wallet [14.4049998196489 tSSC] ; Staked [68.1950000033819 tSSC]
2024-01-13 15:41:20,453 SUCCESS | subspace.watcher | Balance at block 962929 2024-01-04 14:41:38.422109: wallet [14.4049998196489 tSSC] ; Staked [68.1950000033819 tSSC]
2024-01-13 15:41:20,465 SUCCESS | subspace.watcher | Balance at block 976221 2024-01-05 14:41:36.422109: wallet [16.3049998197721 tSSC] ; Staked [68.1950000033819 tSSC]
2024-01-13 15:41:20,479 SUCCESS | subspace.watcher | Balance at block 989513 2024-01-06 14:41:34.422109: wallet [18.6049998199268 tSSC] ; Staked [68.1950000033819 tSSC]
2024-01-13 15:41:20,493 SUCCESS | subspace.watcher | Balance at block 1002805 2024-01-07 14:41:32.422109: wallet [22.4049998200236 tSSC] ; Staked [68.1950000033819 tSSC]
2024-01-13 15:41:20,505 SUCCESS | subspace.watcher | Balance at block 1016097 2024-01-08 14:41:30.422109: wallet [27.5049998202194 tSSC] ; Staked [68.1950000033819 tSSC]
2024-01-13 15:41:20,518 SUCCESS | subspace.watcher | Balance at block 1029389 2024-01-09 14:41:28.422109: wallet [32.3049998205333 tSSC] ; Staked [68.1950000033819 tSSC]
2024-01-13 15:41:20,535 SUCCESS | subspace.watcher | Balance at block 1042681 2024-01-10 14:41:26.422109: wallet [37.6049998207868 tSSC] ; Staked [68.1950000033819 tSSC]
2024-01-13 15:41:20,546 SUCCESS | subspace.watcher | Balance at block 1055973 2024-01-11 14:41:24.422109: wallet [40.9049998210348 tSSC] ; Staked [68.1950000033819 tSSC]
2024-01-13 15:41:20,560 SUCCESS | subspace.watcher | Balance at block 1069265 2024-01-12 14:41:22.422109: wallet [42.6049998210348 tSSC] ; Staked [68.1950000033819 tSSC]
2024-01-13 15:41:20,569 SUCCESS | subspace.watcher | Balance at block 1082557 2024-01-13 14:41:20.422109: wallet [3.8049998623373 tSSC] ; Staked [111.094999824462 tSSC]
2024-01-13 15:41:20,569 INFO | subspace.watcher | Between 2024-01-03 14:41:40.422109 and 2024-01-04 14:41:38.422109, stake change =  0 tSSC, wallet change = 0 tSSC
2024-01-13 15:41:20,570 INFO | subspace.watcher | Between 2024-01-04 14:41:38.422109 and 2024-01-05 14:41:36.422109, stake change =  0 tSSC, wallet change = 1.90000000012322 tSSC
2024-01-13 15:41:20,570 INFO | subspace.watcher | Between 2024-01-05 14:41:36.422109 and 2024-01-06 14:41:34.422109, stake change =  0 tSSC, wallet change = 2.30000000015467 tSSC
2024-01-13 15:41:20,570 INFO | subspace.watcher | Between 2024-01-06 14:41:34.422109 and 2024-01-07 14:41:32.422109, stake change =  0 tSSC, wallet change = 3.80000000009686 tSSC
2024-01-13 15:41:20,570 INFO | subspace.watcher | Between 2024-01-07 14:41:32.422109 and 2024-01-08 14:41:30.422109, stake change =  0 tSSC, wallet change = 5.10000000019581 tSSC
2024-01-13 15:41:20,570 INFO | subspace.watcher | Between 2024-01-08 14:41:30.422109 and 2024-01-09 14:41:28.422109, stake change =  0 tSSC, wallet change = 4.80000000031385 tSSC
2024-01-13 15:41:20,570 INFO | subspace.watcher | Between 2024-01-09 14:41:28.422109 and 2024-01-10 14:41:26.422109, stake change =  0 tSSC, wallet change = 5.30000000025347 tSSC
2024-01-13 15:41:20,570 INFO | subspace.watcher | Between 2024-01-10 14:41:26.422109 and 2024-01-11 14:41:24.422109, stake change =  0 tSSC, wallet change = 3.30000000024807 tSSC
2024-01-13 15:41:20,571 INFO | subspace.watcher | Between 2024-01-11 14:41:24.422109 and 2024-01-12 14:41:22.422109, stake change =  0 tSSC, wallet change = 1.7 tSSC
2024-01-13 15:41:20,571 INFO | subspace.watcher | Between 2024-01-12 14:41:22.422109 and 2024-01-13 14:41:20.422109, stake change =  42.8999998210797 tSSC, wallet change = -38.7999999586975 tSSC

````

# Dependencie

this code as a `req.txt` wich containt some library pretty safe and one about substrate.
https://github.com/polkascan/py-substrate-interface