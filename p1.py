from mininet.link import TCLink, Intf from subprocess import call 
 
def myNetwork(): 
 
    net = Mininet( topo=None, 
                   build=False, 
                   ipBase='10.0.0.0/8') 
 
    info( '*** Adding controller\n' )     c0=net.addController(name='c0',                       controller=RemoteController, 
                      ip='192.168.56.105', 
                      protocol='tcp',    port=6633) 
 
    info( '*** Add switches\n') 
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)     s5 = net.addSwitch('s5', cls=OVSKernelSwitch)     s3 = net.addSwitch('s3', cls=OVSKernelSwitch)     s1 = net.addSwitch('s1', cls=OVSKernelSwitch)     s2 = net.addSwitch('s2', cls=OVSKernelSwitch) 
 
    info( '*** Add hosts\n') 
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defau ltRoute=None, mac="00:00:00:00:00:02") 
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defau ltRoute=None, mac="00:00:00:00:00:01") 
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defau ltRoute=None, mac="00:00:00:00:00:04") 
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defau ltRoute=None, mac="00:00:00:00:00:03") 
 
    info( '*** Add links\n')     net.addLink(s1, s2)     net.addLink(s2, s5)     net.addLink(s5, h3)     net.addLink(s5, h4)     net.addLink(h1, s1)     net.addLink(s1, h2)     net.addLink(s1, s4)     net.addLink(s4, s5)     net.addLink(s3, s5)     net.addLink(s1, s3) 
 
    info( '*** Starting network\n') 
    net.build() 
    info( '*** Starting controllers\n') 
    for controller in net.controllers: 
        controller.start() 
 
    info( '*** Starting switches\n') 
    net.get('s4').start([])     net.get('s5').start([c0])     net.get('s3').start([])     net.get('s1').start([c0])     net.get('s2').start([c0]) 
 
    info( '*** Post configure switches and hosts\n')     s4.cmd('ifconfig s4 10.0.0.24')     s5.cmd('ifconfig s5 10.0.0.25')     s3.cmd('ifconfig s3 10.0.0.23')     s1.cmd('ifconfig s1 10.0.0.21')     s2.cmd('ifconfig s2 10.0.0.22') 
 
    CLI(net) 
    net.stop() 
 
if __name__ == '__main__': 
    setLogLevel( 'info' )     myNetwork() 