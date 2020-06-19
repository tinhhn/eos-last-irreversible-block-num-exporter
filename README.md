# eos-last-irreversible-block-num-exporter
EOS last block number exporter
![EOS](https://seeklogo.com/images/E/eos-logo-ECF31E0936-seeklogo.com.png)

##Run a test
```bash
docker run -d -p 8889:8889 -e INTERVAL=5 -e BLOCKCHAIN_FULLNODE_URL=http://your-fullnode:8888 tinhgin/eos-last-irreversible-block-num-exporter
```