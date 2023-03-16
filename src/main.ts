import { createApp } from "vue";
import App from "./App.vue";
import Ban from "./components/layouts/Ban.vue"
import axios from "axios";

// import "~/styles/element/index.scss";

// import ElementPlus from "element-plus";
// import all element css, uncommented next line
// import "element-plus/dist/index.css";

// or use cdn, uncomment cdn link in `index.html`

import "~/styles/index.scss";
import 'uno.css'

// If you want to use ElMessage, import it.
import "element-plus/theme-chalk/src/message.scss"

const response = await axios.get('http://localhost:5000/login')
console.log(response.data)
const app = createApp(App);
const ban = createApp(Ban);
if(response.data.situation == false)
    
    // app.use(ElementPlus);
    app.mount("#app");
else
{
    ban.mount("#app");
}

