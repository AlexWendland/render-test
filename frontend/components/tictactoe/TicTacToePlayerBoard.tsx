import { Button } from "@heroui/button";
import clsx from "clsx";
import { useTicTacToeContext } from "@/components/tictactoe/TicTacToeContext";

export function TicTacToePlayerBoard() {
  const {
    history,
    players,
    currentMove,
    currentPlayer,
    winner,
    winningLine,
    currentUserPosition,
    currentViewedMove,
    setCurrentViewedMove,
    updateCurrentUserPosition,
    makeMove,
  } = useTicTacToeContext();

  const availablePlayers = [
    { id: 0, name: "Cross", icon: <img src="/cross.png" width="30" /> },
    { id: 1, name: "Nought", icon: <img src="/nought.png" width="30" /> },
  ];

  return (
    <div className="w-full max-w-sm border rounded-xl p-4 bg-gray-50 shadow-md">
      <h2 className="text-center text-xl font-semibold mb-4">Players</h2>
      <div className="space-y-3">
        {availablePlayers.map((player) => {
          const isSelected = currentUserPosition === player.id;
          return (
            <Button
              key={player.id}
              variant="light"
              className={clsx(
                "flex items-center justify-between w-full px-4 py-2 text-left",
                isSelected && "border-blue-500 bg-blue-50",
              )}
              onPress={() => {
                if (currentUserPosition == player.id) {
                  updateCurrentUserPosition(null);
                } else {
                  updateCurrentUserPosition(player.id);
                }
              }}
            >
              <span className="flex items-center space-x-2">
                <span>{player.icon}</span>
                <span>{player.name}</span>
              </span>
              <span className="text-sm text-gray-700">
                {players[player.id]} {isSelected && "(*)"}
              </span>
            </Button>
          );
        })}
      </div>
    </div>
  );
}
