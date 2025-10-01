---
{
  "id": "chapter-128",
  "title": "Domain Name System",
  "order": 128,
  "source": {
    "href": "c11.xhtml",
    "anchor": "head-2-202"
  },
  "est_tokens": 3886,
  "slug": "domain-name-system",
  "meta": {
    "nav_title": "Domain Name System",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Domain Name System

There are three numbering and addressing concepts you should be familiar with:

- Doman Name The domain name or computer name is a “temporary” human-friendly convention assigned to an IP address.

- IP Address The IP address is a “temporary” logical address assigned over or onto the MAC address.

- MAC Address The MAC address, or hardware address, is a “permanent” physical address.

# “Permanent” and “Temporary” Addresses

The reason these two adjectives are within quotation marks is that they are not completely accurate. MAC addresses are designed to be permanent physical addresses but often can be changed. When the NIC supports the change, the change occurs on the hardware. When the OS supports the change, the change is only in memory, but it looks like a hardware change to all other network entities (this is known as MAC spoofing ).

An IP address is temporary because it is a logical address and could be changed at any time, either by DHCP or by an administrator. However, there are instances where systems are statically assigned an IP address. Likewise, computer names or DNS names might appear permanent, but they are logical and thus able to be modified by an administrator.

Domain Name System (DNS) resolves a human-friendly domain name into its IP address equivalent. Then, Address Resolution Protocol (ARP) (see the later section “ARP Concerns”) resolves the IP address into its MAC address equivalent. It is also possible to resolve an IP address into a domain name via a DNS reverse lookup if a PTR (i.e., pointer) resource record is defined in the domain's zone file. IP addresses are assigned either statically or dynamically via DHCP.

DNS is the hierarchical naming scheme used in both public and private networks. DNS links IP addresses and human-friendly fully qualified domain names (FQDNs) together. An FQDN consists of three main parts:

- Top-level domain (TLD) —The com in www.google.com

`com`

- Registered domain name —The google in www.google.com

`google`

- Subdomain(s) or hostname —The www in www.google.com

`www`

The TLD can be any number of official options, including six of the original seven TLDs— com , org , edu , mil , gov , and net —as well as many newer ones, such as info , museum , telephone , mobi , biz , and so on. There are also two-letter country variations known as country codes . (See www.iana.org/domains/root/db for details on current TLDs and country codes.) The seventh original TLD was int , for international, which was replaced by the two-letter country codes.

`com`

`org`

`edu`

`mil`

`gov`

`net`

`info`

`museum`

`telephone`

`mobi`

`biz`

`int`

The registered domain name must be officially registered with one of any number of approved domain registrars, such as Network Solutions ( networksolutions.com ) or IONOS ( ionos.com ).

The far-left section of an FQDN can be either a single hostname, such as www. , ftp. , blog. , images. , and so on, or a multisectioned subdomain designation, such as server1.group3.bldg5.myexamplecompany.com .

`www.`

`ftp.`

`blog.`

`images.`

The total length of an FQDN can't exceed 253 characters (including the dots). Any single section can't exceed 63 characters. FQDNs can only contain letters, numbers, and hyphens. Though not typically shown, there is a dot to the right of the TLD, which represents the root of the entire DNS namespace.

Every registered domain name has an assigned authoritative name server. The primary authoritative name server hosts the original editable zone file for the domain. Secondary authoritative name servers can be used to host read-only copies of the zone file. A zone file is the collection of resource records or details about the specific domain. There are dozens of possible resource records (see www.iana.org/assignments/dns-parameters/dns-parameters.xhtml ) such as A records linking an FQDN to an IPv4 address and AAAA records linking an FQDN to an IPv6 address.

Originally, DNS was handled by a static local file known as the hosts file. The hosts file contains hard-coded references for domain names and their associated IP addresses. This file still exists on most TCP/IP capable computers, but a dynamic DNS query system has mostly replaced it. Administrators or hackers can add content to the hosts file.

`hosts`

`hosts`

`hosts`

When client software points to an FQDN, the resolution process first checks the local DNS cache to see whether the answer is already known. The DNS cache consists of the preloaded local hosts file plus any DNS query results (that haven't timed out). If the needed answer isn't in the cache, a DNS query is sent to the DNS server indicated in the local IP configuration. The rest of the process of resolving the query is interesting and complex, but most of it isn't relevant to the (ISC) 2 CISSP exam.

`hosts`

DNS operates over TCP and UDP port 53. TCP port 53 is used for zone transfers. These are zone file exchanges between DNS servers, for special manual queries, or when a response exceeds 512 bytes. UDP port 53 is used for most typical DNS queries.

Domain Name System Security Extensions (DNSSEC) ( dnssec.net ) is a security improvement to the existing DNS infrastructure. The primary function of DNSSEC is to provide mutual certificate authentication and encrypted sessions between devices during DNS operations. DNSSEC has been implemented across a significant portion of the DNS system. Once fully implemented, DNSSEC will significantly reduce server-focused DNS abuses, such as zone file poisoning and DNS cache poisoning. However, DNSSEC only applies to DNS servers, not to systems performing queries against DNS servers (such as clients).

Non-DNS servers (i.e., mostly client devices), especially when using the internet, should consider using DNS over HTTPS (DoH) . This system creates an encrypted session with a DNS server of TLS-protected HTTP and then uses that session as a form of VPN to protect the DNS query and response. A late 2020 enhancement to DoH is Oblivious DoH (ODoH) . ODoH adds a DNS proxy between the client and the DNS resolver so that the identity of the requesting client is isolated from the DNS resolver. Thus, ODoH provides anonymity and privacy to DNS queries.

For an excellent primer and advanced discussion on DNS, its operation, and known issues, please visit “An Illustrated Guide to the Kaminsky DNS Vulnerability”: unixwiz.net/techtips/iguide-kaminsky-dns-vuln.html .

### DNS Poisoning

DNS poisoning is the act of falsifying the DNS information used by a client to reach a desired system. It can take place in many ways. Whenever a client needs to resolve a DNS name into an IP address, it may go through the following process:

- Check the local cache (which includes content from the hosts file).

`hosts`

- Send a DNS query to a known DNS server.

- Send a broadcast query to any possible local subnet DNS server. (This step isn't widely supported.)

If the client doesn't obtain a DNS-to-IP resolution from any of these steps, the resolution fails and the communication can't be sent. There are many ways to attack or exploit DNS, most of which are used to return false results.

#### Rogue DNS Server

A rogue DNS server can listen in on network traffic for any DNS query or specific DNS queries related to a target site. Then the rogue DNS server sends a DNS response to the client with false IP information. Once the client receives the response from the rogue DNS server, the client closes the DNS query session, which causes the response from the real DNS server to be dropped and ignored as an out-of-session packet.

DNS queries are not authenticated, but they do contain a 16-bit value known as the query ID (QID) . The DNS response must include the same QID as the query to be accepted. Thus, a rogue DNS server must include the requesting QID in the false reply.

#### Performing DNS Cache Poisoning

DNS poisoning involves attacking DNS servers and placing incorrect information into its zone file or cache. Authorized DNS server attacks aim at altering the primary record of an FQDN in the zone file on the primary authoritative DNS server. This causes real DNS servers to send false data back to clients. However, an attack on an authoritative DNS server typically gets noticed very quickly, so it rarely results in widespread exploitation.

So, most attackers focus on caching DNS servers instead. A caching DNS server is any DNS system deployed to cache DNS information from other DNS servers. The content hosted on a caching DNS server is not being watched by the worldwide security community but just the local operators. Thus, an attack against a caching DNS server can potentially occur without notice for a significant period of time. This variation can be called DNS cache poisoning .

Although both of these attacks focus on DNS servers, they ultimately affect clients. Once a client has performed a dynamic DNS resolution, the information received from an authoritative DNS server or a caching DNS server will be temporarily stored in the client's local DNS cache. If that information is false, then the client's DNS cache has been poisoned.

#### DNS Pharming

Another attack closely related to DNS poisoning and/or DNS spoofing is DNS pharming . Pharming is the malicious redirection of a valid website's URL or IP address to a fake website. Pharming typically occurs either by modifying the local hosts file on a system or by poisoning or spoofing DNS resolution.

`hosts`

#### Altering the Hosts File

Modifying the hosts file on the client by placing false DNS data into it redirects users to false locations. If an attacker is able to plant false information into the hosts file, then when the system boots the contents of the hosts file they will be read into memory where they will take precedence. This attack is effective, but it is also highly targeting. It only affects the individual systems with a locally corrupted hosts file. If the attacker wishes to cause harm more broadly, any of the other methods would be more effective.

`hosts`

`hosts`

`hosts`

`hosts`

#### Corrupt the IP Configuration

Corrupting the IP configuration can result in a client having a false DNS server definition (i.e., DNS lookup address changing). The DNS server address is typically distributed to clients through DHCP, but it can also be assigned statically. Attacks to alter a client's DNS server lookup address can be performed by compromising DHCP or through a script.

#### DNS Query Spoofing

A DNS query spoofing attack occurs when the hacker is able to eavesdrop on a client's query to a DNS server. The attacker then sends back a reply with false information. In order for this to be successful, the false reply must include the correct QID cloned from the query.

#### Use Proxy Falsification

Although not strictly a DNS issue, a proxy falsification attack could be implemented via DNS if the proxy's domain name has to be resolved by the client to use the proxy. Attacks could modify the local configuration, the configuration script, or the routing table to redirect communications to a false proxy. This method works only against web communications (or other services or protocols that use a proxy). A rogue proxy server can modify traffic packets to reroute requests to whatever site the hacker wants.

An on-path attack (also known as a man-in-the-middle attack, or MitM) can be performed using DNS abuses, such as DNS cache poisoning. Once a client receives a response from DNS, that response will be cached for future use. If false information can be fed into the DNS cache, then misdirecting communications is trivially easy. See Chapter 17 , “Preventing and Responding to Incidents,” for more on this type of attack.

#### Defenses to DNS Poisoning

Although there are many DNS poisoning methods, here are some basic security measures you can take that can greatly reduce their threat:

- Limit zone transfers from internal DNS servers to external DNS servers. This is accomplished by blocking inbound TCP port 53 (zone transfer requests) and UDP port 53 (queries).

- Require internal clients to resolve all domain names through the internal DNS. This will require that you block outbound UDP port 53 (for queries) while keeping open outbound TCP port 53 (for zone transfers).

- Limit the external DNS servers from which internal DNS servers pull zone transfers.

- Deploy a network intrusion detection system (NIDS) to watch for abnormal DNS traffic.

- Properly harden all DNS, server, and client systems in your private network.

- Use DNSSEC to secure your DNS infrastructure.

- Use DoH or ODoH on all clients where supported.

There is no easy patch or update that will prevent these exploits from being waged against a client. This is due to the fact that these attacks take advantage of the normal and proper mechanisms built into various protocols, services, and applications. Thus, the defense is more of a detective and preventive concern. Install both HIDS and NIDS tools to watch for abuses of these types. Regularly review the logs of your DNS and DHCP systems, as well as local client system logs and potentially firewall, switch, and router logs for entries indicating abnormal or questionable occurrences.

Organizations should use a split-DNS system (aka split-horizon DNS , split-view DNS , and split-brain DNS ). A split-DNS is deploying a DNS server for public use and a separate DNS server for internal use. All data in the zone file on the public DNS server is accessible by the public via queries or probing. However, the internal DNS is for internal use only. Only internal systems are granted access to interact with the internal DNS server. Outsiders are prohibited from accessing the internal DNS server by blocking inbound port 53 for both TCP and UDP. TCP 53 is used for zone transfers (which includes most DNS server–to–DNS server communications), and UDP 53 is used for queries (which is any non-DNS system sending a query to a DNS server). Internal systems can be configured to only interact with the internal DNS servers, or they may be allowed to send queries to external DNS servers (which does require the firewall to be a stateful inspection firewall configured to allow responses to return to the internal system from an approved outbound query).

Another DNS defense mechanism is a DNS sinkhole. A DNS sinkhole is a specific example of a false telemetry system (aka sinkhole server, internet sinkhole, and blackhole DNS). This technique is effectively DNS spoofing used as a defense. A DNS sinkhole attempts to provide false responses to DNS queries from malware, such as bots, to prevent access to command and control systems. It can also be used to protect users from visiting known malicious or phishing sites. Thus, DNS sinkholes can be used for both malicious and benign/investigative/defensive purposes.

### Domain Hijacking

Domain hijacking , or domain theft , is the malicious action of changing the registration of a domain name without the authorization of the valid owner. This may be accomplished by stealing the owner's logon credentials, using XSRF, hijacking a session, using an on-path/MitM attack, or exploiting a flaw in the domain registrar's systems.

An example of a domain hijack is the theft of the fox-it.com domain; you can read about this attack at www.fox-it.com/en/news/blog/fox-it-hit-by-cyber-attack .

Sometimes when another person registers a domain name immediately after the original owner's registration expires, it is called domain hijacking, but it should not be. This is a potentially unethical practice, but it is not an actual hack or attack. It is taking advantage of the oversight of the original owner's failure to manually extend their registration or configure auto-renewal. If an original owner loses their domain name by failing to maintain registration, there is often no recourse other than to contact the new owner and ask about reobtaining control.

When an organization loses their domain and someone else takes over control, this can be a devastating event both to the organization and its customers and visitors. The new FQDN owner might host completely different content or a false duplicate of the previous site. This later activity might result in fooling visitors, similar to a phishing attack, where personally identifiable information (PII) might be extracted and collected.

The best defense against domain hijacking is to use strong multifactor authentication when logging into your domain registrar. To defend against letting your domain registration lapse, set up auto-renew and double-check the payment method a week before the renewal date.

#### Typosquatting

Typosquatting is a practice employed to take advantage of when a user mistypes the domain name or IP address of an intended resource. A squatter predicts URL typos and then registers those domain names to direct traffic to their own site. The variations used for typosquatting include common misspellings (such as googel.com ), typing errors (such as gooogle.com ), variations on a name or word (for example, plurality, as in googles.com ), and different top-level domains (TLDs) such as google.edu .

`google.edu`

#### Homograph Attack

Another DNS, address, or hyperlink concern is that of the homograph attack . These attacks leverage similarities in character sets to register phony international domain names (IDNs) that to the naked eye appear legitimate. For example, in many fonts, some letters in Cyrillic look like Latin characters; for example, the l (i.e., lowercase L) in Latin looks like the Palochka Cyrillic letter. Thus, domain names of apple.com and paypal.com might look valid as Latin characters but could actually include Cyrillic characters that when resolved direct you to a different site than you intended. For a thorough discussion of the homograph attack, see blog.malwarebytes.com/101/2017/10/out-of-character-homograph-attacks-explained .

#### URL Hijacking

URL hijacking refers to the practice of displaying a link or advertisement that looks like that of a well-known product, service, or site, but when clicked redirects the user to an alternate location, service, or product. This may be accomplished by posting sites and pages and exploiting search engine optimization (SEO), or through the use of adware that replaces legitimate ads and links with those leading to alternate or malicious locations.

#### Clickjacking

Clickjacking is a means to redirect a user's click or selection on a web page to an alternate often malicious target instead of the intended and desired location. One means of clickjacking is to add an invisible or hidden overlay, frame, or image map over the displayed page. The user sees the original page, but any mouse click or selection will be captured by the floating frame and redirected to the malicious target.
