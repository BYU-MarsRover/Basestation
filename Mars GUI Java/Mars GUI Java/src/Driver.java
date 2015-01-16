//Following code from:  http://stackoverflow.com/questions/17902236/java-send-udp-packet-with-data
import java.net.DatagramPacket;		//reader and writer
import java.net.InetAddress;		//reader and writer
import java.net.DatagramSocket;		//writer
import java.net.MulticastSocket;	//reader

public class Driver {
	
	//Writer
	final DatagramSocket socketWrite = new DatagramSocket();
	final String MULTICAST_GROUP_ID = "10.10.149.253";
	final int PORT = 27015;
	byte[] buf1 = new byte[256];
	buf1 = "Hello World!".getBytes();
	final InetAddress group = InetAddress.getByName(MULTICAST_GROUP_ID);
	DatagramPacket packet1 = new DatagramPacket(buf1, buf1.length, group, PORT);
	socketWrite.send(packet1);
	socketWrite.close();

	//Reader
	final MulticastSocket socketRead = new MulticastSocket(PORT);
	final InetAddress address = InetAddress.getByName(MULTICAST_GROUP_ID);
	socketRead.joinGroup(address);
	byte[] buf2 = new byte[256];
	DatagramPacket packet2 = new DatagramPacket(buf2, buf2.length);
	socketRead.receive(packet2);
	String received = new String(packet2.getData());
	socketRead.leaveGroup(address);
	socketRead.close();
	
}
