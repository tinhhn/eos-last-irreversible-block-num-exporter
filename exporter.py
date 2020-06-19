from prometheus_client import start_http_server, Gauge
import logging, sys, os, json, time, urllib.request

logger = logging.getLogger('EOS_LAST_BLOCK_NUM')
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

g = Gauge('eos_last_block_num', 'EOS Last Block')

def get_eos_lib_block(url):
    try:
        f = urllib.request.urlopen(url + '/v1/chain/get_info')
        data = json.loads(f.read().decode('utf-8'))
        metric = data['last_irreversible_block_num']
        return metric
    except Exception as e:
        logger.debug(e)

if __name__ == '__main__':
    try:
        sleeptime = int(os.environ['INTERVAL'])
        logger.info("Environment variable INTERVAL=%s" % sleeptime)
    except:
        sleeptime = 10
        logger.debug("Environment variable INTERVAL is not set. Use default INTERVAL=%s" % sleeptime)
    try:
        url = os.environ['BLOCKCHAIN_FULLNODE_URL']
        logger.info("Environment variable BLOCKCHAIN_FULLNODE_URL=%s" % url)
    except:
        url = "http://127.0.0.1:8888"
        logger.debug("Environment variable BLOCKCHAIN_FULLNODE_URL is not set. Use default BLOCKCHAIN_FULLNODE_URL=%s" % url)

    # Start up the server to expose the metrics.
    start_http_server(8889)
    # Generate some requests.
    while True:
        time.sleep(sleeptime)
        try:
            g.set(get_eos_lib_block(url))
        except Exception as e:
            logger.debug(e)