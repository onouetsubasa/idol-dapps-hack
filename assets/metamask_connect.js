window.addEventListener('load', function () {
    if (typeof web3 !== 'undefined') {
        console.log('Web3：' + web3.currentProvider.constructor.name);
        startApp();
    }else{
        alert('MetaMaskをインストールして下さい')
    }
})

const startApp = () => {
    web3.eth.getAccounts((error, accounts) => {
        if (error) return;
        //TODO: 動的化する
        //let user_account = accounts[0];
        let user_account = '0x2b5af53e4d1277271c440d0b7209bf50b8d42b94'
        //let user_account = '0x808E8C4190141aC686D6Cb84D44410937ACa3C07'
        if(typeof user_account !== 'undefined'){
            //console.log('user_account');
            //console.log(user_account);
            getBalance(user_account);
        }else{
            console.log("ログインして下さい")
        }
    })
}

//アドレスのETH量を取得
const getBalance = _address => {
    web3.eth.getBalance(_address, (error, balance) => {
        if (error) return;
        console.log(JSON.stringify(balance, null, 2));
    })
}

export default web3;