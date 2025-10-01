---
{
  "id": "chapter-105",
  "title": "Infrastructure as Code",
  "order": 105,
  "source": {
    "href": "c09.xhtml",
    "anchor": "head-2-172"
  },
  "est_tokens": 736,
  "slug": "infrastructure-as-code",
  "meta": {
    "nav_title": "Infrastructure as Code",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Infrastructure as Code

Infrastructure as code (IaC) is a change in how hardware management is perceived and handled. Instead of seeing hardware configuration as a manual, direct hands-on, one-on-one administration hassle, it is viewed as just another collection of elements to be managed in the same way that software and code are managed under DevSecOps (security, development, and operations). With IaC, the hardware infrastructure is managed in much the same way that software code is managed, including: version control, predeployment testing, custom-crafted test code, reasonableness checks, regression testing, and consistency in a distributed environment.

This alteration in hardware management approach has allowed many organizations to streamline infrastructure changes so that they occur more easily, more rapidly, more securely and safely, and more reliably than before. IaC often uses definition files and rule sets that are machine readable to quickly deploy new settings and manage hardware consistently and efficiently. These files can be treated as software code in terms of development, testing, deployment, updates, and management. IaC is not just limited to hardware; it can also be used to oversee and manage virtual machines (VMs), storage area networks (SANs), and software-defined networking (SDN). IaC often requires the implementation of hardware management software, such as Puppet. Such solutions provide version control, continuous integration, and code review to the portion of an IT infrastructure that was not able to be managed in this manner in the past.

### Immutable Architecture

Immutable architecture is the concept that a server never changes once it is deployed. If there is a need to update, modify, fix, or otherwise alter, a new server is built or cloned from the current one, the necessary changes are applied, and then the new server is deployed to replace the previous one. Once the new server is validated, the older server is decommissioned. VMs are destroyed and the physical hardware/system is reused for future deployments.

The benefits of immutable architecture are reliability, consistency, and a predictable deployment process. It eliminates issues common in mutable infrastructures where midstream updates and changes can cause downtime, data loss, or incompatibility.

The mindset of immutable architecture is often described with the analogy of pets versus cattle or snowflakes versus phoenixes. If a server is treated like a pet, when something goes wrong, everyone marshals to the rescue. However, if a server is treated like cattle, when something goes wrong, it is taken out back and shot, and another is brought in to replace it. If a server is managed uniquely, then it is a snowflake and requires specific focus and attention, causing an increase in administrative time and attention, not to mention complexity for the environment. If a server is always built from scratch, then when changes are needed a new system can be created with integrated improvements through automated processes, thus rising from the ashes (of previous decommissioned servers) like a phoenix. This minimizes administrative overhead, reduces deployment time, and maintains consistency in the environment.

A derivative of IaC and DCE is software-defined networking (SDN). SDN is the management of networking as a virtual or software resource even though it technically still occurs over hardware. That is the same concept as IaC which treats the management of hardware as concept that can be managed in a means similar to how software can be managed. Similarly, just as DCE is a collection of individual systems that work together to support a resource or provide a service, so to is SDN a collection of hardware and software elements that are designed to provide a virtualization of networking management and control. Please see Chapter 11 for details on software-defined networking (SDN).
