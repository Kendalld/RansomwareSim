# RansomwareSim

<img src="img/RansomWareSim.png"></img>

This is a fork of the (RansomwareSim)[https://github.com/HalilDeniz/RansomwareSim.git] by Halil Deniz
<h4 align="center">
<br>
   <a href="https://buymeacoffee.com/halildeniz" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
</h4>

## Usage and Disclaimer
**`Important`:** This tool should only be used in controlled environments where all participants have given consent. Do not use this tool on any system without explicit permission. For more, read [SECURE](SECURITY.md)

RansomwareSim is developed for educational purposes only. The creators of RansomwareSim are not responsible for any misuse of this tool. This tool should not be used in any unauthorized or illegal manner. Always ensure ethical and legal use of this tool.


## Overview
RansomwareSim is a simulated ransomware application developed for educational and training purposes. It is designed to demonstrate how ransomware encrypts files on a system and communicates with a command-and-control server. This tool is strictly for educational use and should not be used for malicious purposes.


## Features
- Encrypts specified file types within a target directory.
- Changes the desktop wallpaper (Windows only).
- Creates&Delete a README file on the desktop with a simulated ransom note.
- Simulates communication with a command-and-control server to send system data and receive a decryption key.
- Decrypts files after receiving the correct key.

## Requirements

- Python 3.x
- cryptography
- colorama

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/Kendalld/RansomwareSim
   ```

2. Navigate to the project directory:

   ```shell
   cd RansomwareSim
   ```

3. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```



### Running the Control Server
1. Open `controlpanel.py`.
2. Start the server by running `controlpanel.py`.
3. The server will listen for connections from `RansomwareSim` and the `Decoder`.
**Note** Leave this as a seperate terminal window open and visable; the decryption key will be displayed here upon encrypting

### Running the Simulator
1. Navigate to the directory containing `RansomwareSim`.
2. Modify the `main` function in `encoder.py` to specify the target directory and other parameters.
3. Run `encoder.py` to start the encryption process.
**Note** Check the controlpanel terminal for activity like shown above. No key data likely means "server_host" not paired correctly from Encoder.py


### Running the Decoder
1. Modify main() function as above
2. Run `decoder.py` after the files have been encrypted.
3. Key output AND decryption input will be on controlpanel window

**Note** rw_TEMPLATE can be used if rw_target contents get corrupted





## License
RansomwareSim is released under the [MIT License](LICENSE). See LICENSE for more information.