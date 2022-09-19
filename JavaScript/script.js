let ipAddress;

window.addEventListener('click',async ()=>{
    alert("Estamos te vendo!!!s")
   let getIpLocation = await fetch('https://api.ipify.org/?format=json');
    let ipJson = await getIpLocation.json(); 
    console.log(ipJson.ip);
    let getLocation = await getLocationInfo(ipJson.ip);
    console.log(getLocation);
    alert(`Your location is ${getLocation.city}, ${getLocation.regionName}, ${getLocation.country} \n E seu IP É ${ipJson.ip}`);
    stopInterval();
    setInterval(openWindow,10000);
})

async function getLocationInfo(ip){
    console.log(`http://ip-api.com/json/${ip}`)
    let response = await fetch(`http://ip-api.com/json/${ip}`);
    let data = await response.json();

    return await data != null || data != undefined? data : {ERROR: "houve algum erro"}
}

let button = `<input type="button" value="Stop interval" id="btn-interval">`

const stopInterval = ()=>{
    document.getElementById('body').append(button);
}

const  openWindow = ()=>{
    let urls = ['www.google.com'];
    urls.forEach(e=> open(e))
};
