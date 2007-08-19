%define major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:		Audiere is a high-level audio API
Name:			audiere
Version:		1.9.4
Release:		%mkrel 2
License:		LGPL
Group:			Development/C++
URL:			http://audiere.sourceforge.net
Source:			http://prdownloads.sourceforge.net/audiere/%{name}-%{version}-src.tar.bz2
Patch0:			%{name}-1.9.4-speex.patch
BuildRequires:		audiofile-devel
BuildRequires:		libflac-devel
BuildRequires:		libcdaudio-devel
BuildRequires:		libogg-devel
BuildRequires:		libvorbis-devel
BuildRequires:		speex-devel
BuildRoot:		%{_tmppath}/%{name}-%{version}-buildroot

%description
Audiere is open source and licensed under the LGPL. This means
that you may freely use Audiere in commercial products, as long
as you do not modify the source code. If you do modify Audiere
and release a product that uses your modifications, you must
release your changes to the code under the LGPL as well.

Audiere is portable. It is tested on Windows, Linux-i386, Cygwin,
and IRIX with at least three major compilers. Most of Audiere is
endian-independent, so I expect it would work with few
modifications on other architectures.

%package -n %{libname}
Summary:	Audiere is a high-level audio API
Group:		System/Libraries

%description -n %{libname}
Audiere is a high-level audio API. It can play Ogg Vorbis, MP3,
FLAC, uncompressed WAV, AIFF, MOD, S3M, XM, and IT files. For
audio output, Audiere supports DirectSound or WinMM in Windows,
OSS on Linux and Cygwin, and SGI AL on IRIX.


%package -n %{develname}
Summary:	Development headers and libraries for audiere
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Requires:	libflac-devel
Requires:	libcdaudio-devel
Requires:	libogg-devel
Requires:	libvorbis-devel
Requires:	speex-devel
Provides:	%{name} = %{version}-%{release}
Provides:	lib%{name} = %{version}-%{release}

%description -n %{develname}
Development headers and libraries for audiere.

%prep
%setup -qn audiere
%patch0 -p1

%build
sh ./bootstrap

%configure2_5x \
	--enable-opt
%make

%install
%makeinstall_std

rm %{buildroot}%{_libdir}/lib*.la

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libaudiere-%{version}.so

%files -n %{develname}
%defattr(-,root,root)
%doc doc/*.txt
%{_bindir}/audiere-config
%{_includedir}/audiere.h
%{_libdir}/libaudiere.a
%{_libdir}/libaudiere.so
