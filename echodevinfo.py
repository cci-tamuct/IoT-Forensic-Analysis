from physical import * #attaches script to ds
import re
import clr
clr.AddReference('System.Windows.Forms')
from System.Windows.Forms import MessageBox

#define the path as a regex
path = '/Root/build.prop$'

#search for file in all file systems
for fs in ds.FileSystems:
	for file in fs.Search(path):
		print file

#read data into a file
data = file.read()

#define regex for finding data in file
regex = 'product.name=(.*)\x0A'
result = re.search(regex, data) #perform a search

#define whatever is in the parenthesis
#and get the offset and length within the file
prodname = result.group(1)
offset = data.find(prodname)
length = len(prodname)

#add the item as a device info object to Physical Analyzer
ds.DeviceInfo.Add('Product Name', prodname, file.Data.GetSubRange(offset, length), 'Recovered Device Info')
MessageBox.Show('You successfully added the Product Name {0}.'.format(prodname), 'Success!!')

#define regex for finding data in file
regex = 'build.id=(.*)\x0A'
result = re.search(regex, data) #perform a search

#define whatever is in the parenthesis
#and get the offset and length within the file
buildid = result.group(1)
offset = data.find(buildid)
length = len(buildid)

#add the item as a device info object to Physical Analyzer
ds.DeviceInfo.Add('Build ID', buildid, file.Data.GetSubRange(offset, length), 'Recovered Device Info')
MessageBox.Show('You successfully added the Build ID {0}.'.format(buildid), 'Success!!')

#define regex for finding data in file
regex = 'build.version.release=(.*)\x0A'
result = re.search(regex, data) #perform a search

#define whatever is in the parenthesis
#and get the offset and length within the file
bvrelease = result.group(1)
offset = data.find(bvrelease)
length = len(bvrelease)

#add the item as a device info object to Physical Analyzer
ds.DeviceInfo.Add('Build Version Release', bvrelease, file.Data.GetSubRange(offset, length), 'Recovered Device Info')
MessageBox.Show('You successfully added the Build Version Release {0}.'.format(bvrelease), 'Success!!')

#define regex for finding data in file
regex = 'build.version.security_patch=(.*)\x0A'
result = re.search(regex, data) #perform a search

#define whatever is in the parenthesis
#and get the offset and length within the file
bvsecuritypatch = result.group(1)
offset = data.find(bvsecuritypatch)
length = len(bvsecuritypatch)

#add the item as a device info object to Physical Analyzer
ds.DeviceInfo.Add('Build Version Security Release', bvsecuritypatch, file.Data.GetSubRange(offset, length), 'Recovered Device Info')
MessageBox.Show('You successfully added the Build Version Security Patch {0}.'.format(bvsecuritypatch), 'Success!!')

#define regex for finding data in file
regex = 'build.date=(.*)\x0A'
result = re.search(regex, data) #perform a search

#define whatever is in the parenthesis
#and get the offset and length within the file
builddate = result.group(1)
offset = data.find(builddate)
length = len(builddate)

#add the item as a device info object to Physical Analyzer
ds.DeviceInfo.Add('Build Date', builddate, file.Data.GetSubRange(offset, length), 'Recovered Device Info')
MessageBox.Show('You successfully added the Build Date {0}.'.format(builddate), 'Success!!')

#define regex for finding data in file
regex = 'build.date.utc=(.*)\x0A'
result = re.search(regex, data) #perform a search

#define whatever is in the parenthesis
#and get the offset and length within the file
builddateutc = result.group(1)
offset = data.find(builddateutc)
length = len(builddateutc)

#add the item as a device info object to Physical Analyzer
ds.DeviceInfo.Add('Build Date UTC', builddateutc, file.Data.GetSubRange(offset, length), 'Recovered Device Info')
MessageBox.Show('You successfully added the Build Date UTC {0}.'.format(builddateutc), 'Success!!')

#define regex for finding data in file
regex = 'build.flavor=(.*)\x0A'
result = re.search(regex, data) #perform a search

#define whatever is in the parenthesis
#and get the offset and length within the file
buildflavor = result.group(1)
offset = data.find(buildflavor)
length = len(buildflavor)

#add the item as a device info object to Physical Analyzer
ds.DeviceInfo.Add('Build Flavor', buildflavor, file.Data.GetSubRange(offset, length), 'Recovered Device Info')
MessageBox.Show('You successfully added the Build Flavor {0}.'.format(buildflavor), 'Success!!')

#define regex for finding data in file
regex = 'product.device=(.*)\x0A'
result = re.search(regex, data) #perform a search

#define whatever is in the parenthesis
#and get the offset and length within the file
productdevice = result.group(1)
offset = data.find(productdevice)
length = len(productdevice)

#add the item as a device info object to Physical Analyzer
ds.DeviceInfo.Add('Product Device', productdevice, file.Data.GetSubRange(offset, length), 'Recovered Device Info')
MessageBox.Show('You successfully added the Product Device {0}.'.format(productdevice), 'Success!!')

#define regex for finding data in file
regex = 'product.board=(.*)\x0A'
result = re.search(regex, data) #perform a search

#define whatever is in the parenthesis
#and get the offset and length within the file
productboard = result.group(1)
offset = data.find(productboard)
length = len(productboard)

#add the item as a device info object to Physical Analyzer
ds.DeviceInfo.Add('Product Board', productboard, file.Data.GetSubRange(offset, length), 'Recovered Device Info')
MessageBox.Show('You successfully added the Product Board {0}.'.format(productboard), 'Success!!')

#define regex for finding data in file
regex = 'product.cpu.abi=(.*)\x0A'
result = re.search(regex, data) #perform a search

#define whatever is in the parenthesis
#and get the offset and length within the file
productcpuabi = result.group(1)
offset = data.find(productcpuabi)
length = len(productcpuabi)

#add the item as a device info object to Physical Analyzer
ds.DeviceInfo.Add('Product CPU ABI', productcpuabi, file.Data.GetSubRange(offset, length), 'Recovered Device Info')
MessageBox.Show('You successfully added the Product CPU ABI {0}.'.format(productcpuabi), 'Success!!')

#define regex for finding data in file
regex = 'product.brand=(.*)\x0A'
result = re.search(regex, data) #perform a search

#define whatever is in the parenthesis
#and get the offset and length within the file
productbrand = result.group(1)
offset = data.find(productbrand)
length = len(productbrand)

#add the item as a device info object to Physical Analyzer
ds.DeviceInfo.Add('Product Brand', productbrand, file.Data.GetSubRange(offset, length), 'Recovered Device Info')
MessageBox.Show('You successfully added the Product Brand {0}.'.format(productbrand), 'Success!!')

#define regex for finding data in file
regex = 'product.model=(.*)\x0A'
result = re.search(regex, data) #perform a search

#define whatever is in the parenthesis
#and get the offset and length within the file
productmodel = result.group(1)
offset = data.find(productmodel)
length = len(productmodel)

#add the item as a device info object to Physical Analyzer
ds.DeviceInfo.Add('Product Model', productmodel, file.Data.GetSubRange(offset, length), 'Recovered Device Info')
MessageBox.Show('You successfully added the Product Model {0}.'.format(productmodel), 'Success!!')

#define regex for finding data in file
regex = 'product.package_name=(.*)\x0A'
result = re.search(regex, data) #perform a search

#define whatever is in the parenthesis
#and get the offset and length within the file
packagename = result.group(1)
offset = data.find(packagename)
length = len(packagename)

#add the item as a device info object to Physical Analyzer
ds.DeviceInfo.Add('Product Package Name', packagename, file.Data.GetSubRange(offset, length), 'Recovered Device Info')
MessageBox.Show('You successfully added the Product Package Name {0}.'.format(packagename), 'Success!!')

#define regex for finding data in file
regex = 'build.configuration=(.*)\x0A'
result = re.search(regex, data) #perform a search

#define whatever is in the parenthesis
#and get the offset and length within the file
buildconfig = result.group(1)
offset = data.find(buildconfig)
length = len(buildconfig)

#add the item as a device info object to Physical Analyzer
ds.DeviceInfo.Add('Build Configuration', buildconfig, file.Data.GetSubRange(offset, length), 'Recovered Device Info')
MessageBox.Show('You successfully added the Build Configuration {0}.'.format(buildconfig), 'Success!!')

#define regex for finding data in file
regex = '.platform=(.*)\x0A'
result = re.search(regex, data) #perform a search

#define whatever is in the parenthesis
#and get the offset and length within the file
platform = result.group(1)
offset = data.find(platform)
length = len(platform)

#add the item as a device info object to Physical Analyzer
ds.DeviceInfo.Add('Platform', platform, file.Data.GetSubRange(offset, length), 'Recovered Device Info')
MessageBox.Show('You successfully added the Platform {0}.'.format(platform), 'Success!!')

#define regex for finding data in file
regex = 'product.config.type=(.*)\x0A'
result = re.search(regex, data) #perform a search

#define whatever is in the parenthesis
#and get the offset and length within the file
prodconfigtype = result.group(1)
offset = data.find(prodconfigtype)
length = len(prodconfigtype)

#add the item as a device info object to Physical Analyzer
ds.DeviceInfo.Add('Product Config Type', prodconfigtype, file.Data.GetSubRange(offset, length), 'Recovered Device Info')
MessageBox.Show('You successfully added the Product Config Type {0}.'.format(prodconfigtype), 'Success!!')

#define regex for finding data in file
regex = 'build.version.number=(.*)\x0A'
result = re.search(regex, data) #perform a search

#define whatever is in the parenthesis
#and get the offset and length within the file
bvnumber = result.group(1)
offset = data.find(bvnumber)
length = len(bvnumber)

#add the item as a device info object to Physical Analyzer
ds.DeviceInfo.Add('Build Version Number', bvnumber, file.Data.GetSubRange(offset, length), 'Recovered Device Info')
MessageBox.Show('You successfully added the Build Version Number {0}.'.format(bvnumber), 'Success!!')

#define regex for finding data in file
regex = 'mktg.fireos=(.*)\x0A'
result = re.search(regex, data) #perform a search

#define whatever is in the parenthesis
#and get the offset and length within the file
fireos = result.group(1)
offset = data.find(fireos)
length = len(fireos)

#add the item as a device info object to Physical Analyzer
ds.DeviceInfo.Add('Build MKTG FireOS', fireos, file.Data.GetSubRange(offset, length), 'Recovered Device Info')
MessageBox.Show('You successfully added the Build MKTG FireOS {0}.'.format(fireos), 'Success!!')

#define regex for finding data in file
regex = 'build.version.name=(.*)\x0A'
result = re.search(regex, data) #perform a search

#define whatever is in the parenthesis
#and get the offset and length within the file
bvname = result.group(1)
offset = data.find(bvname)
length = len(bvname)

#add the item as a device info object to Physical Analyzer
ds.DeviceInfo.Add('Build Version Name', bvname, file.Data.GetSubRange(offset, length), 'Recovered Device Info')
MessageBox.Show('You successfully added the Build Version Name {0}.'.format(bvname), 'Success!!')

#define the path as a regex
path = 'Root/misc/wifi/wpa_supplicant.conf$'

#search for file in all file systems
for fs in ds.FileSystems:
	for file in fs.Search(path):
		print file

#read data into a file
data = file.read()

#define regex for finding data in file
regex = 'ssid=\x22(.*)\x22\x0A'
result = re.search(regex, data) #perform a search

#define whatever is in the parenthesis
#and get the offset and length within the file
ssid = result.group(1)
offset = data.find(ssid)
length = len(ssid)

#add the item as a device info object to Physical Analyzer
ds.DeviceInfo.Add('SSID', ssid, file.Data.GetSubRange(offset, length), 'Recovered Device Info')
MessageBox.Show('You successfully added the SSID {0}.'.format(ssid), 'Success!!')

#define regex for finding data in file
regex = 'psk=\x22(.*)\x22\x0A'
result = re.search(regex, data) #perform a search

#define whatever is in the parenthesis
#and get the offset and length within the file
psk = result.group(1)
offset = data.find(psk)
length = len(psk)

#add the item as a device info object to Physical Analyzer
ds.DeviceInfo.Add('PSK', psk, file.Data.GetSubRange(offset, length), 'Recovered Device Info')
MessageBox.Show('You successfully added the PSK {0}.'.format(psk), 'Success!!')

#define regex for finding data in file
regex = 'uuid=(.*)\x0A'
result = re.search(regex, data) #perform a search

#define whatever is in the parenthesis
#and get the offset and length within the file
uuid = result.group(1)
offset = data.find(uuid)
length = len(uuid)

#add the item as a device info object to Physical Analyzer
ds.DeviceInfo.Add('UUID', uuid, file.Data.GetSubRange(offset, length), 'Recovered Device Info')
MessageBox.Show('You successfully added the UUID {0}.'.format(uuid), 'Success!!')

#define regex for finding data in file
regex = 'serial_number=(.*)\x0A'
result = re.search(regex, data) #perform a search

#define whatever is in the parenthesis
#and get the offset and length within the file
serialnumber = result.group(1)
offset = data.find(serialnumber)
length = len(serialnumber)

#add the item as a device info object to Physical Analyzer
ds.DeviceInfo.Add('Serial Number', serialnumber, file.Data.GetSubRange(offset, length), 'Recovered Device Info')
MessageBox.Show('You successfully added the Serial Number {0}.'.format(serialnumber), 'Success!!')

#define the path as a regex
path = 'Root/data/amazon.speech.sim/files/device_capabilities_api.amazonalexa.com$'

#search for file in all file systems
for fs in ds.FileSystems:
	for file in fs.Search(path):
		print file

#read data into a file
data = file.read()

#define regex for finding data in file
regex = 'friendlyName\x22\x3A\x22(.*?)\x22\x2C\x22'
result = re.search(regex, data) #perform a search

#define whatever is in the parenthesis
#and get the offset and length within the file
friendlyname = result.group(1)
offset = data.find(friendlyname)
length = len(friendlyname)

#add the item as a device info object to Physical Analyzer
ds.DeviceInfo.Add('Friendly Name', friendlyname, file.Data.GetSubRange(offset, length), 'Recovered Device Info')
MessageBox.Show('You successfully added the Friendly Name {0}.'.format(friendlyname), 'Success!!')