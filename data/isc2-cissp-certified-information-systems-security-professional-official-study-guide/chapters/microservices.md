---
{
  "id": "chapter-104",
  "title": "Microservices",
  "order": 104,
  "source": {
    "href": "c09.xhtml",
    "anchor": "head-2-171"
  },
  "est_tokens": 540,
  "slug": "microservices",
  "meta": {
    "nav_title": "Microservices",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Microservices

It is important to evaluate and understand the vulnerabilities in system architectures, especially in regard to technology and process integration. As multiple technologies and complex processes are intertwined in the act of crafting new and unique business functions, new issues and security problems often surface. As systems are integrated, attention should be paid to potential single points of failure as well as to emergent weaknesses in service-oriented architecture (SOA) . An SOA constructs new applications or functions out of existing but separate and distinct software services. The resulting application is often new; thus, its security issues are unknown, untested, and unprotected. All new deployments, especially new applications or functions, need to be thoroughly vetted before they are allowed to go live into a production network or the public internet.

Microservices are an emerging feature of web-based solutions and are derivative of SOA. A microservice is simply one element, feature, capability, business logic, or function of a web application that can be called upon or used by other web applications. It is the conversion or transformation of a capability of one web application into a microservice that can be called upon by numerous other web applications.

Microservices are often created as a means to provide purpose-specific business capabilities through services that are independently deployed. Often, microservices are small and focused on a singular operation, designed with few dependencies, and are based on fast short-term development cycles (similar to Agile). It is also common to deploy microservices based on immutable architecture or infrastructure as code.

Microservices are a popular development strategy because they allow large complex solutions to be broken into smaller self-contained functions. This design also enables multiple programming groups to work on crafting separate elements or microservices simultaneously. The relationship to an application programming interface (API) is that each microservice must have a clearly defined (and secured!) API to allow for I/O between multiple microservices as well as to and from other applications. Microservices are a type of programming or design architecture, whereas APIs are a standardized framework to facilitate communications and data exchange.

A service delivery platform (SDP) is a collection of components that provide the architecture for service delivery. SDP is often used in relation to telecommunications, but it can be used in many contexts, including VoIP, Internet TV, SaaS, and online gaming. An SDP is similar to a content delivery network (CDN) (see Chapter 11 ), as both are designed for the support of and efficient delivery of a resource (such as services of a SDP and multimedia of a CDN). The goal of an SDP is to provide transparent communication services to other content or service providers. Both SDPs and CDNs can be implemented using microservices.
