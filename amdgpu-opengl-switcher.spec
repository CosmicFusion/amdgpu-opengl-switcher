Name:          amdgpu-opengl-switcher
Version:       2.0
Release:       0%{?dist}
License:       GPL
Group:         Unspecified
Summary:       Select needed OpenGL implementation with gl_mesa, gl_zink or gl_pro prefix


URL:           https://github.com/Ashark/archlinux-amdgpu-pro/blob/master/progl

Source0:        %{name}-%{version}-%{release}.x86_64.tar.gz




Provides:      amdgpu-opengl-switcher = %{version}-%{release}
Provides:      amdgpu-opengl-switcher(x86-64) = %{version}-%{release}
Requires:      /usr/bin/bash

%install
tar -xf %{SOURCE0}
mv usr %{buildroot}/

%description
Select needed opengl implementation with gl_mesa, gl_zink or gl_pro prefix
%files
%attr(0755, root, root) "/usr/bin/gl_zink"
%attr(0755, root, root) "/usr/bin/gl_pro"
%attr(0755, root, root) "/usr/bin/gl_mesa"
%attr(0644, root, root) "/usr/share/bash-completion/completions/gl_zink"
%attr(0644, root, root) "/usr/share/bash-completion/completions/gl_pro"
%attr(0644, root, root) "/usr/share/bash-completion/completions/gl_mesa"

