{ pkgs, ... }: {
  channel = "stable-24.05"; # ou "unstable"

  # Pacotes que serão instalados no ambiente
  packages = [
    pkgs.python3
    pkgs.python3Packages.flask
    pkgs.python3Packages.requests
  ];

  idx = {
    extensions = [ "ms-python.python" ];
    workspace = {
      onCreate = {
        install = ''
          python -m venv .venv
          source .venv/bin/activate
          pip install --upgrade pip
          # ainda instala as libs extras que você colocar no requirements.txt
          pip install -r requirements.txt || true
        '';
        default.openFiles = [ "README.md" "src/index.html" "main.py" ];
      };
    };
    previews = {
      enable = true;
      previews = {
        web = {
          command = [ "./devserver.sh" ];
          env = { PORT = "$PORT"; };
          manager = "web";
        };
      };
    };
  };
}
