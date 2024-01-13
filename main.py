import click

from log_utils import init_logger
from engine import Substrate


@click.command()
@click.option('--node_rpc', '-n', default='ws://127.0.0.1:9944', type=str, help='node rpc url (do not forget to enable cors & rpc external)')
@click.option('--wallet', '-w', default='st8VCipcz7xezUnM73T7szCiyNau51YYJAGovKGETUjuPy5oj', type=str, help='wallet to watch')
@click.option('--block_interval', '-b', default='13292', type=int, help='number of block between occurence (around a day for 13292)')
@click.option('--occurence', '-o', default='10', type=int, help='number of occurence')
@click.option('--debug', '-d', is_flag=True, default=False, help='Enable debug if specified')
def start_report(node_rpc: str, wallet: str, block_interval: int, occurence: int, debug: bool):
    logger = init_logger(debug)
    SubstrateWrapper = Substrate(node_rpc, wallet, block_interval, occurence)
    SubstrateWrapper.get_balance()
    SubstrateWrapper.get_stats()


if __name__ == '__main__':
    start_report()

