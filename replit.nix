{ pkgs }: {
  deps = [
    pkgs.glibcLocales
    pkgs.bashInteractive
    pkgs.nodePackages.bash-language-server
    pkgs.man
  ];
}