# This it avoid calling perl so many times
%{expand:%%define	perl_vendorarch	%{perl_vendorarch}}
%{expand:%%define	perl_vendorlib	%{perl_vendorlib}}
#
Summary:	Common dirs for Perl modules
Summary(pl.UTF-8):	Katalogi wspólne dla modułów Perla
Name:		perl-dirs
Version:	1.0
Release:	15
License:	Public Domain
Group:		Development/Languages/Perl
BuildRequires:	perl-base
Requires:	%{perl_vendorarch}
Requires:	%{perl_vendorlib}
Provides:	%{name}(%{_target_cpu})
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Common dirs for Perl modules.

%description -l pl.UTF-8
Katalogi wspólne dla modułów Perla.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{perl_vendorarch},%{perl_vendorlib}}

while read dir; do
	install -d $RPM_BUILD_ROOT$dir
done <<EOF
%{perl_vendorarch}/AI
%{perl_vendorarch}/Algorithm
%{perl_vendorarch}/Astro
%{perl_vendorarch}/Audio
%{perl_vendorarch}/Authen
%{perl_vendorarch}/B
%{perl_vendorarch}/BSD
%{perl_vendorarch}/Bit
%{perl_vendorarch}/Chemistry
%{perl_vendorarch}/Class
%{perl_vendorarch}/Compress
%{perl_vendorarch}/Compress/Raw
%{perl_vendorarch}/Convert
%{perl_vendorarch}/Crypt
%{perl_vendorarch}/Crypt/OpenSSL
%{perl_vendorarch}/Data
%{perl_vendorarch}/DateTime
%{perl_vendorarch}/Devel
%{perl_vendorarch}/Device
%{perl_vendorarch}/Digest
%{perl_vendorarch}/Encode
%{perl_vendorarch}/File
%{perl_vendorarch}/IPC
%{perl_vendorarch}/Image
%{perl_vendorarch}/Inline
%{perl_vendorarch}/IO
%{perl_vendorarch}/Linux
%{perl_vendorarch}/Locale
%{perl_vendorarch}/Math
%{perl_vendorarch}/Math/BigInt
%{perl_vendorarch}/Net
%{perl_vendorarch}/Ogg
%{perl_vendorarch}/Ogg/Vorbis
%{perl_vendorarch}/PerlIO
%{perl_vendorarch}/Speech
%{perl_vendorarch}/Speech/Recognizer
%{perl_vendorarch}/String
%{perl_vendorarch}/Sub
%{perl_vendorarch}/Sys
%{perl_vendorarch}/Template
%{perl_vendorarch}/Term
%{perl_vendorarch}/Text
%{perl_vendorarch}/Time
%{perl_vendorarch}/Unicode
%{perl_vendorarch}/Unix
%{perl_vendorarch}/WWW
%{perl_vendorarch}/XML
%{perl_vendorarch}/auto/AI
%{perl_vendorarch}/auto/Algorithm
%{perl_vendorarch}/auto/Astro
%{perl_vendorarch}/auto/Audio
%{perl_vendorarch}/auto/Authen
%{perl_vendorarch}/auto/BSD
%{perl_vendorarch}/auto/Bit
%{perl_vendorarch}/auto/Chemistry
%{perl_vendorarch}/auto/Class
%{perl_vendorarch}/auto/Clone
%{perl_vendorarch}/auto/Compress
%{perl_vendorarch}/auto/Compress/Raw
%{perl_vendorarch}/auto/Convert
%{perl_vendorarch}/auto/Crypt
%{perl_vendorarch}/auto/Crypt/OpenSSL
%{perl_vendorarch}/auto/Data
%{perl_vendorarch}/auto/Devel
%{perl_vendorarch}/auto/Device
%{perl_vendorarch}/auto/Digest
%{perl_vendorarch}/auto/Encode
%{perl_vendorarch}/auto/File
%{perl_vendorarch}/auto/IPC
%{perl_vendorarch}/auto/Image
%{perl_vendorarch}/auto/Inline
%{perl_vendorarch}/auto/IO
%{perl_vendorarch}/auto/Linux
%{perl_vendorarch}/auto/Locale
%{perl_vendorarch}/auto/Math
%{perl_vendorarch}/auto/Math/BigInt
%{perl_vendorarch}/auto/Net
%{perl_vendorarch}/auto/Ogg
%{perl_vendorarch}/auto/Ogg/Vorbis
%{perl_vendorarch}/auto/PerlIO
%{perl_vendorarch}/auto/Regexp
%{perl_vendorarch}/auto/Speech
%{perl_vendorarch}/auto/Speech/Recognizer
%{perl_vendorarch}/auto/String
%{perl_vendorarch}/auto/Sub
%{perl_vendorarch}/auto/Sys
%{perl_vendorarch}/auto/Term
%{perl_vendorarch}/auto/Text
%{perl_vendorarch}/auto/Time
%{perl_vendorarch}/auto/Unicode
%{perl_vendorarch}/auto/Unix
%{perl_vendorarch}/auto/WWW
%{perl_vendorarch}/auto/XML
%{perl_vendorlib}/AI
%{perl_vendorlib}/AI/NeuralNet
%{perl_vendorlib}/Algorithm
%{perl_vendorlib}/Apache
%{perl_vendorlib}/Apache2
%{perl_vendorlib}/App
%{perl_vendorlib}/App/Packer
%{perl_vendorlib}/Archive
%{perl_vendorlib}/Array
%{perl_vendorlib}/Astro
%{perl_vendorlib}/Attribute
%{perl_vendorlib}/Audio
%{perl_vendorlib}/Authen
%{perl_vendorlib}/B
%{perl_vendorlib}/Barcode
%{perl_vendorlib}/Bundle
%{perl_vendorlib}/Business
%{perl_vendorlib}/CGI
%{perl_vendorlib}/Cache
%{perl_vendorlib}/Carp
%{perl_vendorlib}/Chart
%{perl_vendorlib}/Cisco
%{perl_vendorlib}/Class
%{perl_vendorlib}/Class/Data
%{perl_vendorlib}/Compress
%{perl_vendorlib}/Config
%{perl_vendorlib}/Convert
%{perl_vendorlib}/Crypt
%{perl_vendorlib}/DBD
%{perl_vendorlib}/DNS
%{perl_vendorlib}/Data
%{perl_vendorlib}/Date
%{perl_vendorlib}/Date/Japanese
%{perl_vendorlib}/DateTime
%{perl_vendorlib}/Devel
%{perl_vendorlib}/Device
%{perl_vendorlib}/Digest
%{perl_vendorlib}/Email
%{perl_vendorlib}/Email/Simple
%{perl_vendorlib}/Error
%{perl_vendorlib}/Exporter
%{perl_vendorlib}/ExtUtils
%{perl_vendorlib}/File
%{perl_vendorlib}/File/Path
%{perl_vendorlib}/Filesys
%{perl_vendorlib}/Font
%{perl_vendorlib}/Games
%{perl_vendorlib}/Getopt
%{perl_vendorlib}/GnuPG
%{perl_vendorlib}/Graph
%{perl_vendorlib}/Graphics
%{perl_vendorlib}/HTML
%{perl_vendorlib}/HTTP
%{perl_vendorlib}/Hash
%{perl_vendorlib}/I18N
%{perl_vendorlib}/IO
%{perl_vendorlib}/IO/Socket
%{perl_vendorlib}/IPC
%{perl_vendorlib}/Image
%{perl_vendorlib}/Inline
%{perl_vendorlib}/Jabber
%{perl_vendorlib}/Language
%{perl_vendorlib}/Lingua
%{perl_vendorlib}/Lingua/EN
%{perl_vendorlib}/Lingua/Stem
%{perl_vendorlib}/Lingua/Stem/Snowball
%{perl_vendorlib}/List
%{perl_vendorlib}/Locale
%{perl_vendorlib}/LockFile
%{perl_vendorlib}/Log
%{perl_vendorlib}/MIME
%{perl_vendorlib}/Mail
%{perl_vendorlib}/Math
%{perl_vendorlib}/Math/BigInt
%{perl_vendorlib}/Math/Business
%{perl_vendorlib}/Math/Calc
%{perl_vendorlib}/Math/Fractal
%{perl_vendorlib}/Modem
%{perl_vendorlib}/Module
%{perl_vendorlib}/Module/Pluggable
%{perl_vendorlib}/Net
%{perl_vendorlib}/Net/IDN
%{perl_vendorlib}/Net/SMTP
%{perl_vendorlib}/NetAddr
%{perl_vendorlib}/NetServer
%{perl_vendorlib}/Netscape
%{perl_vendorlib}/News
%{perl_vendorlib}/Number
%{perl_vendorlib}/OLE
%{perl_vendorlib}/Object
%{perl_vendorlib}/PAR
%{perl_vendorlib}/PHP
%{perl_vendorlib}/Params
%{perl_vendorlib}/Parse
%{perl_vendorlib}/PerlIO
%{perl_vendorlib}/PerlIO/via
%{perl_vendorlib}/Pod
%{perl_vendorlib}/PostScript
%{perl_vendorlib}/Proc
%{perl_vendorlib}/Quantum
%{perl_vendorlib}/RADIUS
%{perl_vendorlib}/RPC
%{perl_vendorlib}/RPM
%{perl_vendorlib}/RTF
%{perl_vendorlib}/Regexp
%{perl_vendorlib}/SNMP
%{perl_vendorlib}/SOAP
%{perl_vendorlib}/SOAP/Transport
%{perl_vendorlib}/SQL
%{perl_vendorlib}/SVN
%{perl_vendorlib}/Schedule
%{perl_vendorlib}/Set
%{perl_vendorlib}/Sort
%{perl_vendorlib}/Speech
%{perl_vendorlib}/Spreadsheet
%{perl_vendorlib}/Statistics
%{perl_vendorlib}/String
%{perl_vendorlib}/Sub
%{perl_vendorlib}/Sys
%{perl_vendorlib}/TeX
%{perl_vendorlib}/Template
%{perl_vendorlib}/Term
%{perl_vendorlib}/Term/ReadLine
%{perl_vendorlib}/Term/Screen
%{perl_vendorlib}/Test
%{perl_vendorlib}/Test/HTTP
%{perl_vendorlib}/Text
%{perl_vendorlib}/Text/Query
%{perl_vendorlib}/Tie
%{perl_vendorlib}/Time
%{perl_vendorlib}/Tree
%{perl_vendorlib}/UNIVERSAL
%{perl_vendorlib}/Unicode
%{perl_vendorlib}/Unix
%{perl_vendorlib}/WebService
%{perl_vendorlib}/WWW
%{perl_vendorlib}/WWW/Google
%{perl_vendorlib}/X500
%{perl_vendorlib}/XML
%{perl_vendorlib}/XML/Filter
%{perl_vendorlib}/XML/Handler
%{perl_vendorlib}/XML/Parser
%{perl_vendorlib}/XML/RSS
%{perl_vendorlib}/XML/XPath
%{perl_vendorlib}/auto
%{perl_vendorlib}/auto/AI
%{perl_vendorlib}/auto/Array
%{perl_vendorlib}/auto/Compress
%{perl_vendorlib}/auto/Config
%{perl_vendorlib}/auto/Crypt
%{perl_vendorlib}/auto/Data
%{perl_vendorlib}/auto/Devel
%{perl_vendorlib}/auto/GnuPG
%{perl_vendorlib}/auto/Mail
%{perl_vendorlib}/auto/Math
%{perl_vendorlib}/auto/Net
%{perl_vendorlib}/auto/Schedule
%{perl_vendorlib}/auto/Statistics
%{perl_vendorlib}/auto/Text
%{perl_vendorlib}/auto/WWW
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/*
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto
