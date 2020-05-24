#
# spec file for package vlc
#
# Copyright (c) 2020 UnitedRPMs.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://goo.gl/zqFJft

%global gitdate 20200524
%global commit0 f507868d1c7cf616e7bfeb4699429f0cee9e574b
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

%bcond_without workaround_circle_deps 
%bcond_without codecs
%bcond_with vaapi
%bcond_without wayland
%bcond_without ffmpeg
# yes, libav
%bcond_with libav 
#
%bcond_with gstreamer

%global _with_bluray    1
%bcond_with opencv 
%bcond_with freerdp
%bcond_with fluidsynth 
%bcond_with vdpau
%bcond_without qt5 
%bcond_with qt4 

%ifarch x86_64 i686
%bcond_without crystalhd
%endif

%if 0%{?fedora} >= 30
%bcond_with placebo
%else
%bcond_without placebo
%endif 

%bcond_without projectM

Summary:	The cross-platform open-source multimedia framework, player and server
Name:		vlc
Version:	3.0.10
Release:	9%{?gver}%{?dist}
Epoch:		1
License:	GPLv2+
Group:		Applications/Multimedia
URL:		http://www.videolan.org
Source0:	https://github.com/videolan/vlc-3.0/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1:	vlc-snapshot
Patch:		vlc-qt5.11.patch
Patch1:	https://github.com/RPi-Distro/vlc/raw/stretch-rpt/debian/patches/mmal_8.patch

BuildRequires:	desktop-file-utils
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	aalib-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	avahi-devel
BuildRequires:	cdparanoia-devel
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	libnfs-devel
BuildRequires:	libarchive-devel
BuildRequires:  libsidplayfp-devel
BuildRequires:  libmpc-devel
%if %{with gstreamer}
BuildRequires:  pkgconfig(gstreamer-app-1.0)
%endif
BuildRequires:  speexdsp-devel
BuildRequires:	openjpeg-devel
BuildRequires:	libmfx-devel
BuildRequires:	fluidsynth-devel
BuildRequires:	libvmmalloc-devel
BuildRequires:  soxr-devel
BuildRequires:  libsecret-devel
BuildRequires:  libnotify-devel

%if %{with ffmpeg}
BuildRequires: ffmpeg-devel >= 4.0
%endif
%if %{with libav}
BuildRequires: libav-devel >= 11.4
%endif
BuildRequires:	flac-devel
%if %{with fluidsynth}
BuildRequires: fluidsynth-devel
%endif
%if %{with freerdp}
BuildRequires: freerdp1-devel
# BuildRequires: freerdp-devel
%endif
BuildRequires:	fribidi-devel
BuildRequires: gnome-vfs2-devel
BuildRequires:	gnutls-devel >= 1.0.17
BuildRequires:	gsm-devel
BuildRequires:	jack-audio-connection-kit-devel
#BuildRequires:	kde-filesystem
BuildRequires:	game-music-emu-devel
BuildRequires:	libavc1394-devel
BuildRequires:	libass-devel >= 0.9.7
%{?_with_bluray:BuildRequires: libbluray-devel >= 0.2.1}
BuildRequires:	libcaca-devel
BuildRequires:	libcddb-devel
BuildRequires:	libcdio-devel >= 0.77-3
BuildRequires:	pkgconfig(libchromaprint)
%if %{with crystalhd}
BuildRequires: libcrystalhd-devel
%endif
BuildRequires:	libdc1394-devel >= 2.1.0
BuildRequires:	libdv-devel
BuildRequires:	libdvdnav-devel
BuildRequires:	libebml-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libid3tag-devel
BuildRequires:	libkate-devel
BuildRequires:	libmatroska-devel >= 0.7.6
BuildRequires:	libmodplug-devel
BuildRequires:	libmp4v2-devel
BuildRequires:	libmpcdec-devel
BuildRequires:	libmtp-devel >= 1.0.0
%if %{with projectM}
%if 0%{?fedora} >= 31
BuildRequires: 	libprojectM-devel 
%else
BuildRequires: 	libprojectM-qt-devel 
%endif
%endif
BuildRequires:	libproxy-devel
BuildRequires:	librsvg2-devel >= 2.9.0
BuildRequires:	libssh2-devel
BuildRequires:	libsysfs-devel
BuildRequires:	libshout-devel
BuildRequires:	libsmbclient-devel
BuildRequires:	libtar-devel
BuildRequires:	libtheora-devel
BuildRequires:	libtiger-devel
BuildRequires:	libtiff-devel
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(libvncclient)
BuildRequires:	libupnp-devel
BuildRequires:	libv4l-devel
%if %{with vaapi}
BuildRequires:  pkgconfig(libva)
BuildRequires:  gstreamer1-vaapi
%endif
%if %{with vdpau}
BuildRequires:  pkgconfig(vdpau)
%endif
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	lirc-devel
BuildRequires:  kernel-headers
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	libmusicbrainz5-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libshout-devel
BuildRequires:	lua-devel
BuildRequires:	minizip-devel
BuildRequires:	ncurses-devel
%if %{with opencv}
BuildRequires: pkgconfig(opencv)
%endif
BuildRequires:	openslp-devel
BuildRequires:	libpng-devel
BuildRequires:	opus-devel
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig(libpulse) >= 0.9.8
%if %{with qt4}
BuildRequires:	qt4-devel qt-x11
%endif

BuildRequires: schroedinger-devel >= 1.0.10
BuildRequires:	sqlite-devel
BuildRequires:	SDL_image-devel
%{?_with_sidplay:BuildRequires: pkgconfig(libsidplay2)}
BuildRequires:	speex-devel >= 1.1.5
BuildRequires:	taglib-devel
BuildRequires: 	vcdimager-devel >= 0.7.21
BuildRequires:	zlib-devel
BuildRequires:	zvbi-devel

# X-libs
BuildRequires:	libXt-devel
BuildRequires:	libXv-devel
BuildRequires:	libXxf86vm-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-devel
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:	xorg-x11-proto-devel

%if %{with workaround_circle_deps}
BuildRequires: phonon-backend-gstreamer
%endif
BuildRequires:	perl-Devel-Pragma
BuildRequires:	git
BuildRequires:	freetype-devel
BuildRequires:	libXinerama-devel
BuildRequires:	libnotify-devel
BuildRequires:	libXi-devel
# Those are dependencies which are NOT provided in Fedora, mostly for legal reasons.
BuildRequires: a52dec-devel
BuildRequires: faad2-devel >= 2.9.1
BuildRequires: libdca-devel
BuildRequires: libdvbpsi-devel
BuildRequires: libmad-devel
BuildRequires: libmpeg2-devel >= 0.3.2 
BuildRequires: twolame-devel
BuildRequires: x264-devel >= 0.157
BuildRequires: x265-devel >= 3.3
BuildRequires: xvidcore-devel
BuildRequires: live555-devel >= 2020.04.06
BuildRequires: mpg123-devel

BuildRequires: libdrm-devel
BuildRequires: libX11-devel
BuildRequires: pkgconfig(libv4l2)

# Fool but it needs detect libva for build...
BuildRequires:  pkgconfig(libva)


# Wayland support
%if %{with wayland}
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: wayland-devel
BuildRequires: qt5-qtwayland-devel
BuildRequires: wayland-protocols-devel
%endif

# Chromecast
BuildRequires:  protobuf-lite-devel
%if 0%{?fedora} >= 26
BuildRequires:	libmicrodns-devel
%endif

# NEW
BuildRequires: cmake
BuildRequires: lirc-devel
%if 0%{?fedora} >= 33
BuildRequires: pkgconfig(dav1d) >= 0.7.0
%else
BuildRequires: pkgconfig(dav1d) 
%endif
%if 0%{?fedora} <= 30
BuildRequires: libaom-devel
%endif

# Necessary if you want skin2
# The skins2 module depends on the Qt interface. Without it you will not be able to open any dialog box from the interface, which makes the skins2 interface rather useless.
%if %{with qt5}
BuildRequires: qt5-qtbase-devel
BuildRequires: pkgconfig(Qt5) >= 5.5
BuildRequires: pkgconfig(Qt5Widgets) >= 5.5
BuildRequires: pkgconfig(Qt5Core) >= 5.5
BuildRequires: pkgconfig(Qt5Gui) >= 5.5
BuildRequires: pkgconfig(Qt5Svg) >= 5.5
BuildRequires: pkgconfig(Qt5X11Extras) >= 5.5
%endif

BuildRequires: flex
BuildRequires: bison

%if %{with placebo}
BuildRequires: libplacebo-devel
%endif

BuildRequires:	clang llvm

Provides: %{name}-xorg = %{version}-%{release}
Requires: vlc-core  = %{version}-%{release}
# Requires: kde-filesystem

Requires: texlive-gnu-freefont
%if %{with qt5}
Requires: qt5-qtbase
%endif
%if %{with vdpau}
Requires: libvdpau-va-gl
%endif
#For xdg-sreensaver
Requires: xdg-utils

%if %{with wayland}
Requires: libwayland-cursor
Requires: libwayland-client
Requires: qt5-qtwayland
%endif

# Play encrypted Blu-ray discs
Recommends: libaacs
Recommends: libbdplus

%description
VLC media player is a highly portable multimedia player and multimedia framework
capable of reading most audio and video formats as well as DVDs, Audio CDs VCDs,
and various streaming protocols.
It can also be used as a media converter or a server to stream in uni-cast or 
multi-cast in IPv4 or IPv6 on networks.


%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name}-core = %{version}-%{release}
Provides:	vlc-devel = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package core
Summary:	VLC media player core
Group:		Applications/Multimedia
Provides:	vlc-nox = %{version}-%{release}
Provides:	vlc-core = %{version}-%{release}
Obsoletes:	vlc-nox < 1.1.5-2


%description core
VLC media player core components

%package extras
Summary:	VLC media player with extras modules
Group:		Applications/Multimedia
Provides:	vlc-extras = %{version}-%{release}
Requires:	vlc-core = %{version}-%{release}


%description extras
VLC media player extras modules.

%package plugin-jack
Summary:	JACK audio plugin for VLC
Group:		Applications/Multimedia
Requires:	vlc-core = %{version}-%{release}
Provides:	vlc-plugin-jack = %{version}-%{release}

%description plugin-jack
JACK audio plugin for the VLC media player.

%if %{with gstreamer}
%package codec-gstreamer
Summary:        Decode using GStreamer for VLC
Group:          Applications/Multimedia
Requires:       %{name} = %{version}-%{release}
Provides:	vlc-codec-gstreamer = %{version}-%{release}

%description codec-gstreamer
This package enhances the functionality of the VLC VideoLAN Client by
using GStreamer as backend to decode videos (incl. GStreamers available
modules).
%endif

%prep

# Our trick; the tarball doesn't download completely the source code; vlc needs some data from .git
# the script makes it for us.

%{S:1} -c %{commit0}

%autosetup -T -D -n vlc-%{shortcommit0} -p1
# qt and wayland need merges forces for solve the DpiScaling and DpiPixmaps
sed -i '/#if HAS_QT56/,+3d' modules/gui/qt/qt.cpp

### And LUA 5.3.4 has some more API changes
sed -i 's/luaL_checkint(/(int)luaL_checkinteger(/' \
    modules/lua/{demux,libs/{configuration,dialog,net,osd,playlist,stream,variables,volume}}.c



echo '********* BOOTSTRAPPING *********'
date


./bootstrap

%build

# PKG_CONFIG_PATH=%{_libdir}/freerdp1/pkgconfig/:%{_libdir}/pkgconfig/:%{_libdir}/libav/pkgconfig/:/opt/freerdp-1.0.2/%{_lib}/pkgconfig/:
#XCFLAGS="-g -O2 -fstack-protector-strong -Wformat -Werror=format-security -D_FORTIFY_SOURCE=2" XLDFLAGS="-Wl,-z,relro"


%if %{with projectM}
sed -e 's:truetype/ttf-dejavu:TTF:g' -i modules/visualization/projectm.cpp
sed -e 's|-Werror-implicit-function-declaration||g' -i configure
sed 's|whoami|echo builduser|g' -i configure
sed 's|hostname -f|echo arch|g' -i configure
%endif


export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib64/

%configure  \
	--disable-dependency-tracking		\
	--disable-optimizations			\
%if 0%{?fedora} >= 22
%ifarch i686
	--disable-mmx --disable-sse		\
%endif
%endif
	--disable-silent-rules			\
	--with-pic				\
	--disable-rpath				\
	--with-binary-version=%{version}	\
        --with-kde-solid=%{_kde4_appsdir}/solid/actions \
	--enable-lua				\
%if %{with opencv}
	--enable-opencv		 		\
%endif
	--enable-realrtsp			\
	--enable-flac				\
	--enable-tremor				\
	--enable-speex				\
	--enable-theora				\
	--enable-libass				\
	--enable-shout				\
        --enable-xvideo 	                \
	--enable-svg				\
	--enable-caca				\
	--enable-jack				\
	--enable-pulse				\
	--enable-ncurses			\
  	--enable-libmpeg2			\
   	--enable-mad				\
   	--enable-avcodec			\
   	--enable-avformat			\
   	--enable-swscale			\
   	--enable-postproc			\
   	--enable-faad				\
   	--enable-a52				\
   	--enable-dca				\
%if %{with placebo}
	--enable-libplacebo			\
%endif
   	--enable-twolame			\
   	--enable-live555			\
   	--enable-v4l2				\
%if %{with vdpau}
	--enable-vdpau				\
%endif
   	--enable-sftp                        	\
   	--disable-svgdec                     	\
	--enable-sout				\
	--enable-freetype                    	\
   	--with-default-font=%{_datadir}/fonts/truetype/FreeSerifBold.ttf \
   	--with-default-monospace-font=%{_datadir}/fonts/truetype/FreeMono.ttf \
	--disable-oss 				\
%if %{with wayland}
	--enable-wayland			\
%else
	--disable-wayland			\
%endif
	--enable-nls 				\
	--enable-opus				\
	--enable-upnp 				\
	--enable-shared 			\
	--disable-static			\
%if %{with vaapi}
        --enable-libva 			\
%else
        --disable-libva 			\
%endif
        --enable-skins2			\
%if %{with freerdp}
	--enable-freerdp	                \		
%endif	
   	--enable-fast-install                   \
	--enable-vlm				\
%if !%{with projectM}
	--disable-projectm			\
%endif
	--enable-dav1d				\
        --enable-lirc  			\ 
echo '********* FINISHED CONFIGURE *********'
date


#./compile
CFLAGS="-fPIC"
make %{?_smp_mflags} V=0 || return 1
#make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p" CPPROG="cp -p" %{?_smp_mflags}
#make DESTDIR=%{buildroot} install %{?_smp_mflags}
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'

desktop-file-install --vendor ""			\
	--dir $RPM_BUILD_ROOT%{_datadir}/applications	\
	--delete-original				\
	--mode 644					\
	$RPM_BUILD_ROOT%{_datadir}/applications/vlc.desktop

#Fix unowned directories
rm -rf $RPM_BUILD_ROOT%{_docdir}/vlc

#Ghost the plugins cache
touch $RPM_BUILD_ROOT%{_libdir}/vlc/plugins.dat


%find_lang %{name}


%post
%{_libdir}/vlc/vlc-cache-gen -f %{_libdir}/vlc &>/dev/null
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor
fi 
%{_bindir}/update-desktop-database %{_datadir}/applications &>/dev/null || :

%post core -p /sbin/ldconfig

%postun
%{_libdir}/vlc/vlc-cache-gen -f %{_libdir}/vlc &>/dev/null
%{_bindir}/update-desktop-database %{_datadir}/applications &>/dev/null
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor
fi || :

%postun core -p /sbin/ldconfig

%posttrans core
%{_libdir}/vlc/vlc-cache-gen -f %{_libdir}/vlc &>/dev/null || :

%post extras
if [ $1 == 1 ] ; then
  %{_libdir}/vlc/vlc-cache-gen -f %{_libdir}/vlc &>/dev/null || :
fi

%post plugin-jack
if [ $1 == 1 ] ; then
  %{_libdir}/vlc/vlc-cache-gen -f %{_libdir}/vlc &>/dev/null || :
fi

%postun extras
if [ $1 == 0 ] ; then
  %{_libdir}/vlc/vlc-cache-gen -f %{_libdir}/vlc &>/dev/null || :
fi

%postun plugin-jack
if [ $1 == 0 ] ; then
  %{_libdir}/vlc/vlc-cache-gen -f %{_libdir}/vlc &>/dev/null || :
fi

%preun core
if [ $1 == 0 ] ; then
  rm -f %{_libdir}/vlc/plugins*.dat
fi || :


%files
%defattr(755, root, root)
%doc AUTHORS COPYING   
%{_datadir}/kde4/apps/solid/actions/vlc*.desktop
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/vlc*.png
%{_datadir}/icons/hicolor/*/apps/vlc*.xpm
%{_datadir}/vlc/skins2/
%{_datadir}/metainfo/vlc.appdata.xml
%{_bindir}/qvlc
%{_bindir}/svlc
# Next release
#{_libexecdir}/vlc/vlc-qt-check
%{_libdir}/vlc/plugins/gui/libqt_plugin.so
%{_libdir}/vlc/plugins/gui/libncurses_plugin.so
%{?_with_gnomevfs:
%{_libdir}/vlc/plugins/access/libaccess_gnomevfs_plugin.so
}
#{_libdir}/vlc/plugins/video_output/libaa_plugin.so
%{_libdir}/vlc/plugins/video_output/libcaca_plugin.so
%{!?_without_xcb:
%{_libdir}/vlc/plugins/access/libxcb_screen_plugin.so
#%{_libdir}/vlc/plugins/video_output/libxcb_glx_plugin.so
%{_libdir}/vlc/plugins/video_output/libxcb_x11_plugin.so
%{_libdir}/vlc/plugins/video_output/libxcb_window_plugin.so
%{_libdir}/vlc/plugins/video_output/libxcb_xv_plugin.so
#{_libdir}/vlc/plugins/video_filter/libpanoramix_plugin.so
}
%{_libdir}/vlc/plugins/gui/libskins2_plugin.so
%if %{with projectM}
%{_libdir}/vlc/plugins/visualization/libprojectm_plugin.so
%endif
%{_libdir}/vlc/plugins/audio_output/libpulse_plugin.so

# Chromecast plugin; maybe we don't need make a subpackage about it...
# /usr/lib64/vlc/plugins/stream_out/libstream_out_chromecast_plugin.so

%files core -f %{name}.lang
%{_bindir}/vlc
%{_bindir}/cvlc
%{_bindir}/nvlc
%{_bindir}/rvlc
%{_bindir}/vlc-wrapper
%exclude %{_datadir}/vlc/skins2
%{_datadir}/vlc/
%{_libdir}/*.so.*
%exclude %{_libdir}/vlc/plugins/gui/libqt_plugin.so
%{?_with_gnomevfs:
%exclude %{_libdir}/vlc/plugins/access/libaccess_gnomevfs_plugin.so
}
%exclude %{_libdir}/vlc/plugins/access/libaccess_jack_plugin.so

%exclude %{_libdir}/vlc/plugins/access/libvcd_plugin.so
%exclude %{_libdir}/vlc/plugins/codec/libsvcdsub_plugin.so

%if %{with crystalhd}
%exclude %{_libdir}/vlc/plugins/codec/libcrystalhd_plugin.so
%endif


%if %{with fluidsynth}
%exclude %{_libdir}/vlc/plugins/codec/libfluidsynth_plugin.so
%endif
%{!?_without_xcb:
%exclude %{_libdir}/vlc/plugins/access/libxcb_screen_plugin.so
%if 0%{?fedora} < 17
%exclude %{_libdir}/vlc/plugins/control/libglobalhotkeys_plugin.so
%endif
#exclude {_libdir}/vlc/plugins/video_output/libaa_plugin.so
%exclude %{_libdir}/vlc/plugins/video_output/libcaca_plugin.so
#exclude %{_libdir}/vlc/plugins/video_output/libxcb_glx_plugin.so
%exclude %{_libdir}/vlc/plugins/video_output/libxcb_x11_plugin.so
%exclude %{_libdir}/vlc/plugins/video_output/libxcb_window_plugin.so
%exclude %{_libdir}/vlc/plugins/video_output/libxcb_xv_plugin.so
#{_libdir}/vlc/plugins/video_filter/libpanoramix_plugin.so
}
%exclude %{_libdir}/vlc/plugins/gui/libskins2_plugin.so
%if %{with opencv}
%exclude %{_libdir}/vlc/plugins/video_filter/libopencv_example_plugin.so
%exclude %{_libdir}/vlc/plugins/video_filter/libopencv_wrapper_plugin.so
%endif

%if %{with projectM}
%exclude %{_libdir}/vlc/plugins/visualization/libprojectm_plugin.so
%endif

%exclude %{_libdir}/vlc/plugins/audio_output/libjack_plugin.so
%exclude %{_libdir}/vlc/plugins/audio_output/libpulse_plugin.so

%if %{with gstreamer}
%exclude %{_libdir}/vlc/plugins/codec/libgstdecode_plugin.so
%endif

%{_libdir}/vlc/
%{_mandir}/man1/vlc*.1*

%files plugin-jack
%{_libdir}/vlc/plugins/access/libaccess_jack_plugin.so
%{_libdir}/vlc/plugins/audio_output/libjack_plugin.so
%if %{with fluidsynth}
%{_libdir}/vlc/plugins/codec/libfluidsynth_plugin.so
%endif

%files extras
%if %{with opencv}
%{_libdir}/vlc/plugins/video_filter/libopencv_example_plugin.so
%{_libdir}/vlc/plugins/video_filter/libopencv_wrapper_plugin.so
%endif
%if %{with crystalhd}
%{_libdir}/vlc/plugins/codec/libcrystalhd_plugin.so
%endif

%{_libdir}/vlc/plugins/access/libvcd_plugin.so
%{_libdir}/vlc/plugins/codec/libsvcdsub_plugin.so

%files devel
%dir %{_includedir}/vlc
%{_includedir}/vlc/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/vlc-plugin.pc
%{_libdir}/pkgconfig/libvlc.pc

%if %{with gstreamer}
%files codec-gstreamer
%{_libdir}/vlc/plugins/codec/libgstdecode_plugin.so
%endif


%changelog

* Sun May 24 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.10-9.gitf507868
- Updated to current commit
- Support for dav1d 0.7.0 

* Sun May 03 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.10-8.gitd331460
- Updated to current commit

* Thu Apr 23 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.10-7.git7f145af
- Updated to 3.0.10

* Thu Apr 09 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.9.2-7.gitd4c1aef
- Updated to 3.0.9.2

* Mon Feb 24 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.9-17.git7f204ee
- Updated to current commit
- Rebuilt for x265

* Thu Feb 13 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.9-16.gitae25ccd
- Updated to current commit

* Sat Feb 08 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.9-15.git094c41b
- Updated to current commit
- Rebuilt for live555

* Sat Jan 11 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.9-14.git21c2a25
- Updated to current commit

* Sun Dec 15 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.9-13.gitd6739e5
- Rebuilt for live555

* Sun Dec 01 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.9-12.gitd6739e5
- Rebuilt for x265

* Fri Nov 22 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.9-11.git3774ec0
- Rebuilt for libdvdread
- Updated to current commit

* Sat Nov 09 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.9-10.gite987d87
- Rebuilt for faad2

* Wed Nov 06 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.9-9.gite987d87
- Updated to current commit
- Rebuilt for live555

* Fri Oct 18 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.9-8.git2d00056
- Rebuilt for dav1d
- Updated to current commit 

* Mon Oct 07 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.9-7.gitf9379f4
- Updated to 3.0.9 

* Mon Sep 09 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.8-12.git1c3a985
- Updated to current commit 

* Thu Aug 15 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.8-11.gitf350b6b
- Updated to current commit called the final release

* Tue Aug 13 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.8-10.git90f510d
- Rebuilt for live555
- Enabled dav1d
- Enabled aom
- Enable fdk

* Fri Aug 02 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.8-9.gitf97c872
- Rebuilt for live555

* Wed Jul 24 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.8-8.git72ab735
- Updated to current commit

* Wed Jul 03 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.8-7.gitf3940db
- Updated to 3.0.8

* Tue Jul 02 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.7.1-10.gitf3940db
- Rebuilt for live555 

* Sat Jun 22 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.7.1-8.gitf3940db
- Rebuilt for x265

* Tue Jun 11 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.7.1-7.gitf3940db
- Updated to 3.0.7.1

* Fri May 24 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.7-13.git86cee31
- Updated to current commit
- Rebuilt for live555 

* Sat May 11 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.7-12.gitab30e09
- Updated to current commit
- Rebuilt for live555 

* Thu Apr 25 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.7-11.git4a5791a
- Updated to current commit
- Rebuilt for live555 

* Mon Apr 08 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.7-10.git4b7656b
- Updated to current commit
- Rebuilt for live555 

* Wed Mar 13 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.7-9.git828e0ce
- Updated to current commit
- Rebuilt for x264 

* Sat Mar 02 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.7-8.gitc31b329
- Updated to current commit
- Rebuilt for live555

* Tue Feb 05 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.7-7.git71bfa08 
- Updated to 3.0.7

* Mon Feb 04 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.6-8.gitdb3e320  
- Rebuilt for live555

* Fri Dec 28 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.6-7.gitfe5495ae  
- Updated to 3.0.6

* Sun Dec 16 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.5-10.git65d6754  
- Rebuilt for live555
- Updated to current commit

* Wed Nov 28 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.5-8.git5bf38c1  
- Updated to current commit
- Rebuilt for live555

* Wed Nov 21 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.5-7.git5bf38c1  
- Updated to current commit

* Mon Oct 22 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.5-6.gite9d8590  
- Rebuilt for live555

* Wed Oct 10 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.5-5.gite9d8590  
- Enabled placebo
- Updated to current commit

* Sun Oct 07 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.5-4.gite43004e  
- Updated to current commit

* Fri Oct 05 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.5-3.git0509396  
- Automatic Mass Rebuild

* Tue Oct 02 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.5-2.git0509396  
- Automatic Mass Rebuild

* Sun Sep 16 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.5-1.git0509396  
- Updated to 3.0.5-1.git0509396

* Sat Sep 15 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.4-8.git5a7ad1b  
- Automatic Mass Rebuild

* Mon Sep 10 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.4-7.git5a7ad1b  
- Automatic Mass Rebuild

* Thu Aug 09 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.4-6.git5a7ad1b
- Updated to current commit and rebuilt for live555

* Thu Jul 26 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.4-5.gita3f3b93
- Updated to current commit

* Sun Jul 08 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.4-4.git74297b7
- Updated to current commit
- Secured to include skins
- Enabled vlm

* Sat Jul 07 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.4-3.gitce3bb87  
- Automatic Mass Rebuild

* Sat Jun 30 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.4-2.gitce3bb87 
- Updated to current commit
- Changed to Xwayland

* Sat Jun 23 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.4-1.git531fb72  
- Updated to 3.0.4-1.git531fb72

* Mon Jun 18 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.3-3.gita4029ac  
- Updated to 3.0.3-3.gita4029ac

* Sun May 27 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.3-2.git232058f  
- Automatic Mass Rebuild

* Fri May 04 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.3-1.git232058f  
- Updated to 3.0.3

* Thu Apr 26 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.2-5.git52d6aeb  
- Automatic Mass Rebuild

* Wed Apr 18 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.2-4.git52d6aeb  
- Updated to 3.0.2-4.git52d6aeb

* Fri Apr 06 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.2-3.git907a01d  
- Updated to 3.0.2-3.git907a01d

* Wed Mar 14 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.2-2.git2dd3785  
- Updated to current commit 

* Fri Mar 09 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.2-1.git9f88cd6  
- Updated to 3.0.2-1.git9f88cd6

* Sat Mar 03 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.1-1.git29c4721  
- Updated to 3.0.1-1.git29c4721

* Sat Feb 24 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.0-8.git3e62c69  
- Automatic Mass Rebuild

* Sun Feb 18 2018 David Vásquez <davidva AT tutanota DOT com> - 3.0.0-7.git3e62c69
- Go back to 3
- Added missed dependency for Chromecast

* Sun Feb 18 2018 David Vásquez <davidva AT tutanota DOT com> - 4.0.0-7.gitc7b40f6
- Updated to 4.0.0-7.gitc7b40f6

* Mon Feb 05 2018 David Vásquez <davidva AT tutanota DOT com> - 4.0.0-6.git3c7c271
- Updated to current commit

* Tue Jan 30 2018 David Vásquez <davidva AT tutanota DOT com> - 4.0.0-5.gitdfd480e
- Updated to current commit

* Tue Jan 16 2018 David Vásquez <davidva AT tutanota DOT com> - 4.0.0-4.gitc521392
- Updated to current commit

* Wed Dec 27 2017 David Vásquez <davidva AT tutanota DOT com> - 4.0.0-3.gita1cb2bd
- Updated to current commit

* Thu Dec 07 2017 David Vásquez <davidva AT tutanota DOT com> - 4.0.0-2.git095d137
- Updated to 4.0.0-2.git095d137

* Thu Nov 16 2017 David Vásquez <davidva AT tutanota DOT com> - 3.0.0-52.gitf7f184f
- Updated to current commit

* Thu Nov 02 2017 David Vásquez <davidva AT tutanota DOT com> - 3.0.0-51.git90af091
- Enabled skins2 manually, automatic was disabled

* Wed Nov 01 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.0-50.git90af091
- Updated to current commit

* Wed Oct 18 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.0-49.gita4b4226  
- Automatic Mass Rebuild

* Tue Oct 10 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.0-48.gita4b4226 
- Updated to current commit

* Thu Oct 05 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.0-47.gitecb9f19  
- Automatic Mass Rebuild

* Sat Sep 30 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.0-46.gitecb9f19  
- Automatic Mass Rebuild

* Tue Sep 26 2017 David Vásquez <davidva AT tutanota DOT com> - 3.0.0-45-gitecb9f19
- Updated for live555 3.0.0-45-gitecb9f19

* Mon Sep 18 2017 David Vásquez <davidva AT tutanota DOT com> - 3.0.0-44-git7ce308c
- Updated for mpg123

* Thu Aug 24 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.0-43.gitbfff719  
- Updated to 3.0.0-43.gitbfff719

* Mon Jul 31 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.0-42.git2b310f3  
- Automatic Mass Rebuild

* Thu Jul 27 2017 David Vásquez <davidva AT tutanota DOT com> - 3.0.0-41-git2b310f3
- Updated to 3.0.0-41-git2b310f3

* Sat Jul 15 2017 David Vásquez <davidva AT tutanota DOT com> - 3.0.0-40-git3ba7de2
- Updated 3.0.0-40-git3ba7de2

* Sun Jul 09 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.0-39.git89b077e  
- Automatic Mass Rebuild

* Tue Jul 04 2017 David Vásquez <davidva AT tutanota DOT com> - 3.0.0-38-git89b077e
- Updated to current commit

* Sun Jun 18 2017 David Vásquez <davidva AT tutanota DOT com> - 3.0.0-37-gitf8b5c60
- Updated to 3.0.0-37-gitf8b5c60
- Vaapi/libva disabled because new commits broken vlc
- Wayland disabled, because vlc does not play nothing in Gnome 3 with wayland

* Tue Jun 13 2017 David Vásquez <davidva AT tutanota DOT com> - 3.0.0-36-git78d3459
- Updated to 3.0.0-36-git78d3459

* Fri May 19 2017 David Vásquez <davidva AT tutanota DOT com> - 3.0.0-34-git4401972
- Updated to 3.0.0-34-git4401972

* Fri Apr 28 2017 David Vásquez <davidva AT tutanota DOT com> - 3.0.0-33-git7305bf3
- Updated to 3.0.0-33-git7305bf3

* Wed Apr 19 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.0-32.git4a4e0c5  
- Automatic Mass Rebuild

* Mon Apr 17 2017 David Vásquez <davidva AT tutanota DOT com> - 3.0.0-31.git4a4e0c5
- Updated to 3.0.0-31-20170417git4a4e0c5

* Thu Apr 06 2017 Pavlo Rudyi <paulcarroty at riseup.net> - 3.0.0-30
- Updated to 20160406
- Fixed nonexistent commit from vlc master

* Mon Apr 03 2017 David Vásquez <davidva AT tutanota DOT com> - 3.0.0-29-20170403git6fc45a5
- Updated to 3.0.0-29-20170403git6fc45a5

* Thu Mar 23 2017 David Vásquez <davidva AT tutanota DOT com> - 3.0.0-28-20170323git4c63614
- Updated to 3.0.0-28-20170323git4c63614
- New changes in source

* Sat Mar 18 2017 David Vásquez <davidva AT tutanota DOT com> - 3.0.0-27-20170318git508452a
- Updated to 3.0.0-27-20170318git508452a

* Tue Mar 07 2017 David Vásquez <davidva AT tutanota DOT com> - 3.0.0-26-20170307git4ae3d6f
- Updated to 3.0.0-26-20170307git4ae3d6f
- Rebuilt for live555

* Thu Mar 02 2017 David Vásquez <davidva AT tutanota DOT com> - 3.0.0-24-20170302git989bc9d
- Updated to 3.0.0-24-20170302git989bc9d

* Sun Feb 26 2017 David Vásquez <davidva AT tutanota DOT com> - 3.0.0-23-20170123gi58baf1d
- Updated to 3.0.0-23-20170226gitcb30cb2

* Tue Jan 24 2017 David Vásquez <davidva AT tutanota DOT com> - 3.0.0-22-20170123gi58baf1d
- Solved mime issues

* Mon Jan 23 2017 David Vásquez <davidva AT tutanota DOT com> - 3.0.0-21-20170123gi58baf1d
- Updated to 3.0.0-20170123gi58baf1d
- Patch with partial solution for HiDPI and qt5, see https://wiki.archlinux.org/index.php/HiDPI#VLC

* Thu Jan 19 2017 David Vásquez <davidva AT tutanota DOT com> - 3.0.0-20-20170119git7641f2b
- Updated to 3.0.0-20170119git7641f2b
- Solved some issues with live555

* Wed Jan 04 2017 David Vásquez <davidva AT tutanota DOT com> - 3.0.0-19-20170104gitf8f5395
- Enabled Wayland support
- Updated to 3.0.0-20170104gitf8f5395, solved some issues with mp4

* Mon Jan 2 2017 Pavlo Rudyi <paulcarroty at riseup.net> - 3.0.0-18
- Updated to the latest snapshot

* Wed Dec 28 2016 Pavlo Rudyi <paulcarroty at riseup.net> - 3.0.0-17
- Updated to 20161228
- enable vaapi
- added Wayland depends

* Tue Nov 22 2016 David Vásquez <davidva AT tutanota DOT com> - 3.0.0-15-20161122gitccfdb5a
- Reverted source, the commit is incomplete
- Snapshot changes for new infrastructure
- Enabled Chromecast support
- Updated to 3.0.0-20161122gitccfdb5a

* Mon Nov 21 2016 Pavlo Rudyi <paulcarroty at riseup.net> - 3.0.0-14
- Update to %{gitdate}

* Wed Oct 05 2016 David Vásquez <davidva AT tutanota DOT com> 3.0.0-12-20161005git636476b
- Updated to 3.0.0-20161005git636476b
- Rebuilt thanks to live555

* Fri Sep 02 2016 David Vásquez <davidva AT tutanota DOT com> 3.0.0-11-20160902git1e5a21b
- Updated to 3.0.0-20160902git1e5a21b

* Mon Aug 15 2016 David Vásquez <davidva AT tutanota DOT com> 3.0.0-10-20160824git3f83cde
- Rebuild with new live555
- Updated to 3.0.0-20160824git3f83cde

* Mon Aug 15 2016 David Vásquez <davidva AT tutanota DOT com> 3.0.0-9-20160815git81bb542
- Updated 3.0.0-20160815git81bb542

* Fri Jul 08 2016 David Vásquez <davidva AT tutanota DOT com> 3.0.0-8-20160708gitca134b9
- Rebuilt for FFmpeg 3.1

* Sun Jun 26 2016 The UnitedRPMs Project (Key for UnitedRPMs infrastructure) <unitedrpms@protonmail.com> - 3.0.0-7.20160608gitbb83680
- Rebuild with new ffmpeg

* Wed Jun 08 2016 David Vásquez <davidva AT tutanota DOT com> 3.0.0-6-20160608-bb83680
- Updated to 3.0.0-20160608-bb83680
- Solved librdp lost

* Sat May 07 2016 David Vásquez <davidva AT tutanota DOT com> 3.0.0-5-20160506-fa5c292
- Conditional build for freerdp

* Fri May 06 2016 David Vásquez <davidva AT tutanota DOT com> 3.0.0-4-20160506-fa5c292
- Updated to 3.0.0-20160506-fa5c292
- Disabled opencv for compatibility

* Tue Apr 26 2016 David Vásquez <davidva AT tutanota DOT com> 3.0.0-20160426-9ce2d2e-3
- Updated to 3.0.0-20160426-9ce2d2e

* Tue Apr 26 2016 David Vásquez <davidva AT tutanota DOT com> 3.0.0-20160426-9ce2d2e-2
- Updated to 3.0.0-20160426-9ce2d2e

* Mon Feb 29 2016 David Vásquez <davidva AT tutanota DOT com> 3.0.0-20160229-10f9493-1
- Updated to 3.0.0-20160229-10f9493

* Mon Feb 08 2016 David Vásquez <davidva AT tutanota DOT com> 2.2.2-2
- Updated to 2.2.2

* Tue Jul 14 2015 David Vásquez <davidva AT tutanota DOT com> - 2.2.1-1
- Updated to 2.2.1 

* Mon Mar 23 2015 David Vásquez <davidva AT tutanota DOT com> - 2.2.0-2
- Updated to 2.2.0 final release
- Enabled freerdp ver.1
- Upstream
