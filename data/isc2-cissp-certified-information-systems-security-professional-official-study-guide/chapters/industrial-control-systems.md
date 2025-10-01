---
{
  "id": "chapter-97",
  "title": "Industrial Control Systems",
  "order": 97,
  "source": {
    "href": "c09.xhtml",
    "anchor": "head-2-163"
  },
  "est_tokens": 1038,
  "slug": "industrial-control-systems",
  "meta": {
    "nav_title": "Industrial Control Systems",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Industrial Control Systems

An industrial control system (ICS) is a form of computer-management device that controls industrial processes and machines, also known as operational technology (OT) . ICSs are used across a wide range of industries, including manufacturing, fabrication, electricity generation and distribution, water distribution, sewage processing, and oil refining. There are several forms of ICS, including distributed control systems (DCSs) , programmable logic controllers (PLCs) , and supervisory control and data acquisition (SCADA) .

DCS units are typically found in industrial process plants where the need to gather data and implement control over a large-scale environment from a single location is essential. An important aspect of DCS is that the controlling elements are distributed across the monitored environment, such as a manufacturing floor or a production line, and the centralized monitoring location sends commands out of those localized controllers while gathering status and performance data. A DCS might be analog or digital in nature, depending on the task being performed or the device being controlled. For example, a liquid flow value DCS would be an analog system, whereas an electric voltage regulator DCS would likely be a digital system.

A DCS focuses on processes and is state driven, whereas SCADA focuses on data-gathering and is event driven. A DCS is used to control processes using a network of sensors, controllers, actuators, and operator terminals and is able to carry out advanced process control techniques. DCS is more suited to operating on a limited scale, whereas SCADA is suitable for managing systems over large geographic areas.

PLC units are effectively single-purpose or focused-purpose digital computers. They are typically deployed for the management and automation of various industrial electromechanical operations, such as controlling systems on an assembly line or a large-scale digital light display (such as a giant display system in a stadium or on a Las Vegas Strip marquee).

A SCADA system can operate as a standalone device, be networked together with other SCADA systems, or be networked with traditional IT systems. SCADA is often referred to as a human-machine interface (HMI) since it enables people to better understand, oversee, manage, and control complex machine and technology systems. SCADA is used to monitor and control a wide range of industrial processes, but it is not able to carry out advanced process control techniques. SCADA can communicate with PLCs and DCS solutions.

Legacy SCADA systems were designed with minimal human interfaces. Often, they used mechanical buttons and knobs or simple LCD screen interfaces (similar to what you might have on a business printer or a GPS navigation device). However, modern networked SCADA devices may have more complex remote-control software interfaces.

A PLC is used to control a single device in a standalone manner. DCS was used to interconnect several PLCs, but within a limited physical range, in order to gain centralized control, management, and oversight through networking. SCADA expanded this to large-scale physical areas to interconnect multiple DCSs and individual PLCs. For example, a PLC can control a single transformer, a DCS can manage a power station, and SCADA can oversee a power grid.

In theory, the static design of SCADA, PLC, and DCS units and their minimal human interfaces should make the system fairly resistant to compromise or modification. Thus, little security was built into these industrial control devices, especially in the past. But there have been several well-known compromises of industrial control systems in recent years; for example, Stuxnet delivered the first-ever-known rootkit to a SCADA system located in a nuclear facility. Many SCADA vendors have started implementing security improvements into their solutions in order to prevent or at least reduce future compromises. However, in practice, SCADA and ICS systems are still often poorly secured, vulnerable, and infrequently updated, and older versions not designed for security are still in widespread use.

Generally, typical security management and hardening processes can be applied to ICS, DCS, PLC, and SCADA systems to improve on whatever security is or isn't present in the device from the manufacturer. Common important security controls include isolating networks, limiting access physically and logically, restricting code to only essential application, and logging all activity.

The ISA99 standards development committee has established and is maintaining guidelines for securing ICS, DCS, PLC, and SCADA systems. Much of their work is integrated into the International Electrotechnical Commission's (IEC) 62443 series of standards. To learn more about these standards, visit www.isa.org and iecee.org . NIST maintains ICS security standards in SP 800-82 ( csrc.nist.gov/publications/detail/sp/800-82/rev-2/final ). North American Electric Reliability Corporation (NERC) maintains its own security guides for ICS as part of the Critical Infrastructure Protection (CIP) standards ( www.nerc.com/pa/Stand/Pages/CIPStandards.aspx ), which are similar to those of European Reference Network for Critical Infrastructure Protection (ERNCIP) ( erncip-project.jrc.ec.europa.eu ).

`erncip-project.jrc.ec.europa.eu`
