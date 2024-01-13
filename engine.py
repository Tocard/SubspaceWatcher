import datetime
import time

from substrateinterface import SubstrateInterface

import log_utils as wp


class Substrate:
    _wallet = []
    _staker = []
    _timestamp = []
    _average_block_time = 6.5

    def __init__(self, node_rpc: str, wallet: str, block_interval: int, occurence: int):
        self.substrate = SubstrateInterface(url=node_rpc)
        self.wallet = wallet
        self.block_interval = block_interval
        self.occurence = occurence
        self.logger = wp.Logger

    def format_balance(self, amount: int):
        amount = format(amount / 10 ** self.substrate.properties.get('tokenDecimals', 0), ".15g")
        return f"{amount} {self.substrate.properties.get('tokenSymbol', 'UNIT')}"

    def get_stats(self):
        for i in range(self.occurence):
            _staker = self._staker[i + 1] - self._staker[i]
            _wallet = self._wallet[i + 1] - self._wallet[i]
            _timestamp = self._timestamp[i]

            self.logger.info('Between {} and {}, stake change =  {}, wallet change = {}'.format(
                datetime.datetime.utcfromtimestamp(
                    _timestamp),
                    datetime.datetime.utcfromtimestamp(
                        self._timestamp[i + 1]),
                    self.format_balance(_staker),
                    self.format_balance(_wallet)))

    def get_balance(self):
        self.logger.info('We assume an average block time of 6.5s for time estimation')
        bloc_info = self.substrate.get_block()['header']
        self.logger.info(
            'Start Counting at block {}, with {} block interval & {} step at {}.'.format(bloc_info['number'],
                                                                                         self.block_interval,
                                                                                         self.occurence,
                                                                                         datetime.datetime.utcfromtimestamp(
                                                                                             time.time())))
        timer = time.time() - (self.occurence * self.block_interval) * self._average_block_time
        base_bloc = bloc_info['number'] - (self.occurence * self.block_interval)
        for i in range(self.occurence + 1):
            block_hash = self.substrate.get_block_hash(base_bloc)

            result = self.substrate.query(
                "System", "Account", [self.wallet], block_hash=block_hash
            )

            free = result.value["data"]["free"]
            reserved = result.value["data"]["reserved"]
            self.logger.success("Balance at block {} {}: wallet [{}] ; Staked [{}]".format(base_bloc,
                                                                                           datetime.datetime.utcfromtimestamp(
                                                                                               timer),
                                                                                           self.format_balance(free),
                                                                                           self.format_balance(
                                                                                               reserved)
                                                                                           ))
            self._staker.append(reserved)
            self._wallet.append(free)
            self._timestamp.append(timer)
            base_bloc = base_bloc + self.block_interval
            timer = timer + self._average_block_time * self.block_interval
