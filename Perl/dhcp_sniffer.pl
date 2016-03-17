#!/usr/bin/perl
use IO::Socket::INET;
use Net::DHCP::Packet;

#procura por outros servidores de dhcp na rede
#Vasco Santos 14/08/2014
#mail: vasco at vslinux dot net

my $pkg = "";
my $savefile="/tmp/dhcp_sniff";

$sock = IO::Socket::INET->new(LocalPort => 67, Proto => "udp", Broadcast => 1)
        or die "socket: $@";

while ($sock->recv($newmsg, 1024)) {
    $packet = Net::DHCP::Packet->new($newmsg);
    $pkg = $packet->toString();

    #my @array = $pkg =~ /DHO_DHCP_SERVER_IDENTIFIER/g;
    my @array = $pkg =~ /DHO_DHCP_SERVER_IDENTIFIER.* = (.*)/g;

    my @array1 = $pkg =~ /DHO_DHCP_REQUESTED_ADDRESS.* = (.*)/g;

    my @array2 = $pkg =~ /DHO_HOST_NAME.* = (.*)/g;


    for ( my $i = 0; $i < scalar( @array ); $i++ )
       {
               system("ping -W 2 -c 1 ".$array[$i]." > /dev/null");
               my $fmac = "arp -D ".$array[$i]."| grep ether| awk '{print \$3}'";
               $fmac = `$fmac`;
                $fmac =~ s/\R//g;

                my $str ="DHCP Server: ".$array[$i].", Mac: ".$fmac.", give IP: ".$array1[$i].", at Hostname: ".$array2[$i]."\n";


                    open(TEXTM, ">>$savefile");
                    printf TEXTM "$str";
                    close (TEXTM);
                    print $str;
        }

        #print @array;

        #print STDERR $packet->toString();
        print $pkg;

