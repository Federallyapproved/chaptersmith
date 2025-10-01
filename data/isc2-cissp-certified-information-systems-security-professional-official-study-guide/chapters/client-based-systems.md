---
{
  "id": "chapter-95",
  "title": "Client-Based Systems",
  "order": 95,
  "source": {
    "href": "c09.xhtml",
    "anchor": "head-2-161"
  },
  "est_tokens": 1924,
  "slug": "client-based-systems",
  "meta": {
    "nav_title": "Client-Based Systems",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Client-Based Systems

Client-based vulnerabilities place the user, their data, and their system at risk of compromise and destruction. A client-side attack is any attack that is able to harm a client. Generally, when attacks are discussed, it's assumed that the primary target is a server or a server-side component. A client-side or client-focused attack is one where the client itself, or a process on the client, is the target. A common example of a client-side attack is a malicious website that transfers malicious mobile code (such as an applet) to a vulnerable browser running on the client. Client-side attacks can occur over any communications protocol, not just Hypertext Transfer Protocol (HTTP). Another potential vulnerability that is client based is the risk of poisoning of local caches.

### Mobile Code

Applets are code objects sent from a server to a client to perform some action. In fact, applets are actually self-contained miniature programs that execute independently of the server that sent them—that is, mobile code. The arena of the web is undergoing constant flux. The use of applets is not as common today as it was in the early 2010s. However, applets are not absent from the web, and most browsers still support them (or still have add-ons present that support them). Thus, even when your organization does not use applets in your internal or public web design, your web browsers could encounter them while surfing the public web.

Imagine a web server that offers a variety of financial tools to web users. One of these tools might be a mortgage calculator that processes a user's financial information and provides a monthly mortgage payment based on the loan's principal and term and the borrower's credit information. Instead of processing this data and returning the results to the client system, the remote web server might send to the local system an applet that enables it to perform those calculations itself. This provides a number of benefits to both the remote server and the end user:

- The processing burden is shifted to the client, freeing up resources on the web server to process requests from more users.

- The client is able to produce data using local resources rather than waiting for a response from the remote server. In many cases, this results in a quicker response to changes in the input data.

- In a properly programmed applet, the web server does not receive any data provided to the applet as input, therefore maintaining the security and privacy of the user's financial data.

However, applets introduce security concerns. They allow a remote system to send code to the local system for execution. Security administrators must take steps to ensure that code sent to systems on their network is safe and properly screened for malicious activity. Also, unless the code is analyzed line by line, the end user can never be certain that the applet doesn't contain a Trojan horse, backdoor, rootkit, ransomware, or some other malware component. For example, the mortgage calculator might indeed transmit sensitive financial information to the web server without the end user's knowledge or consent.

Two historical examples of applet types are Java applets and ActiveX controls. Java is a platform-independent programming language developed by Sun Microsystems (now owned by Oracle). ActiveX controls were Microsoft's answer to Sun's Java applets. Java is still in use for internal development and business software, but its use on the internet is rare. ActiveX is now a now legacy technology and is both EOL and EOS. It was only supported by Internet Explorer. Most modern internet-capable systems no longer support these applet forms, but it is important to ensure that before assuming a system is secure.

Although Java and ActiveX are no longer in use on or over the internet, JavaScript is. JavaScript is the most widely used mobile code scripting language in the world and is embedded into (included inside of) HTML documents using <script></script> enclosure tags. JavaScript is dependent on its HTML host document. It cannot operate as a standalone script file. Thus, it is not an applet—it is embedded code. However, that means it is automatically downloaded along with the primary web documents from any web server you access, since 95 percent of websites use JavaScript. JavaScript enables dynamic web pages and supports web applications as well as a plethora of client-side activities and page behaviors.

`<script></script>`

JavaScript is supported by most browsers via a dedicated JavaScript engine. Most of the implementations use sandbox isolation to restrict JavaScript to web-related activities while minimizing its ability to perform general-purpose programming tasks. Also, most browsers default to enforcing the same-origin policy. The same-origin policy prohibits JavaScript code from accessing content from another origin. The origin is typically defined by a combination of protocol (i.e., HTTP vs. HTTPS), domain/IP address, and port number. If other content has any one of these origin elements different from the origin of the JavaScript code, the code will be blocked from accessing that content.

However, there are ways of abusing JavaScript. Hackers can create believable fake websites that look and act like a valid site, including duplicating the JavaScript dynamic elements. But since the JavaScript code is in the HTML document sent to the browser, a malicious hacker could alter that code to perform harmful actions, such as copying or cloning credentials and distributing them to the attacker. Malicious hackers have also found means to breach the sandbox isolation and even violate same-original policies from time to time, so JavaScript should be considered a threat. Whenever you allow code from an unknown and thus untrusted source to execute on your system, you are putting your system at risk of compromise. XSS and XSRF/CSRF can be used to exploit JavaScript support in browsers.

Here are some responses to these risks:

- Keep browsers updated (client side).

- Implement JavaScript subsets (such as ADsafe, Secure ECMAScript [SES], or Caja) (server side).

- Use a content security policy (CSP) that attempts to rigidly enforce same-origin restrictions for most browser-side active technologies (integrated into browsers and referenced by HTML header values).

As with most web applications, insertion attacks are common, so watch out for injection of odd or abusive JavaScript code in the input being received by a web server.

As a client, you may gain some benefit by being behind a web application firewall (WAF) or next-generation firewall (NGFW). We do not recommended disabling JavaScript outright—that would cause most of the web to stop functioning in your browser. Instead, the use of add-ons, browser helper objects (BHOs), and extensions may reduce the risk of JavaScript. Two examples include NoScript for Mozilla Firefox and UBlock Origin for Chrome and Edge (based on Chromium).

Another legacy internet applet or remote code technology is Flash. Adobe Flash (although invented by FutureWave, which was acquired by Macromedia, which was acquired by Adobe) was a means to create dynamic web elements, such as animations, web applications, games, utilities, and more. The popularity of Flash peaked in the mid-2000s. Flash has fallen out of favor due to early smartphones lacking support, the fact that it was a closed platform, and the existence of numerous security issues. Adobe declared December 31, 2020 to be EOL for Flash. Until the late 2010s, many browsers included native Flash support. This was replaced with an add-on Flash player (thus, native support was removed from most browsers). However, in 2021, most browsers will block even the Flash add-on.

For more on web-related vulnerabilities, attacks, and countermeasures, see Chapter 21 , “Malicious Code and Application Attacks.”

### Local Caches

There are many types of local caches, including DNS cache, ARP cache, and temporary internet files. See Chapter 11 for details about DNS cache and ARP cache abuses.

Temporary internet files or the internet files cache is the temporary storage of files downloaded from internet sites that are being held by the client's utility (typically a browser) for current and possibly future use. Mostly this cache contains website content, but other internet services can use a file cache as well. A variety of exploitations, such as the split-response attack, can cause the client to download content and store it in the cache that was not an intended element of a requested web page. DOM XSS may be able to access and use locally cached files to execute malicious code or exfiltrate data (see Chapter 21 ). Mobile code scripting attacks could also be used to plant false content in the cache. Once files have been poisoned in the cache, then even when a legitimate web document calls on a cached item, the malicious item will be activated.

Client utilities should be managing the local files cache, but those utilities might not always be doing the best job. Often the defaults are for efficiency and performance, not for security. Consider reconfiguring the cache to only retain files for a short period of time, minimize the cache size, and disable preloading of content. Keep in mind that these changes can reduce browsing performance when on slower or high-latency connections. You may want to configure the browser to delete all cookies and cache upon exit. Although you can typically perform a manual cache wipe, you would have to remember to do that. Another option is to use an automated that can be configured to wipe temporary internet files on a schedule or upon targeted program close.

Additional coverage of client-based endpoint security concerns is in Chapter 11 .
