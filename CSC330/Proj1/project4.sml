datatype token = INT | MAI | RET | OP | CP | OB | CB | SC | IN of int;

(* Helper function to identify if a character is a delimiter or a special C symbol. *)
fun isDelimiterOrSymbol c = List.exists (fn x => x = c) [#" ", #"\n", #"(", #")", #"{", #"}", #";"];

(* Updated tokenize function to handle symbols and whitespace as delimiters, preserving the original sequence of tokens. *)
fun tokenize (str: string) =
    let
        val chars = String.explode str  (*Explode string into list of chars*)
        fun isStandaloneToken c = List.exists (fn x => x = c) [#"(", #")", #"{", #"}", #";"]            (*check is character c is a standalone token*)
        fun extractTokens ([], acc, tokens) = List.rev (if acc = "" then tokens else acc :: tokens)     (*if char list empty, acc is added to tokens (if acc not empty) and return tokens*)
          | extractTokens (c::cs, acc, tokens) =                                                        (*if there are still more char in list*)
            if Char.isSpace c then                                                                          (*if char is space*)
                extractTokens (cs, "", if acc = "" then tokens else acc :: tokens)                              (*accumulator is added to tokens and extractTokens is called again with empty acc*)
            else if isStandaloneToken c then                                                                (*else if char is a standalone token*)
                let
                    val newTokens = if acc = "" then tokens else acc :: tokens                                  (*acc is added to tokens (if acc not empty) then newTokens is set to tokens*)
                in
                    extractTokens (cs, "", (String.str c) :: newTokens)                                         (*continue token extraction with rest of chars and the standalone token c is added to the newTokens list*)
                end
            else                                                                                            (*else, the token is neither space or standalone token*)
                extractTokens (cs, acc ^ String.str c, tokens)                                                  (*continue token extraction and append current token to acc*)
    in
        extractTokens (chars, "", [])                                                                   (*start tokenization with list of characters (exploded string) and an empty acc and token list*)
    end;

(* Function to map string tokens to the corresponding token datatype, handling integers specifically. *)
fun mapStringToToken str =
    case str of
         "int" => SOME INT
       | "main" => SOME MAI
       | "return" => SOME RET
       | "(" => SOME OP
       | ")" => SOME CP
       | "{" => SOME OB
       | "}" => SOME CB
       | ";" => SOME SC
       | _ => (case Int.fromString str of
                    SOME num => SOME (IN num)
                  | NONE => NONE)

(* Main parse function: reads file content, tokenizes it, and maps to tokens, handling invalid cases. *)
fun parse filename =
    let
        val ins = TextIO.openIn filename
        val content = TextIO.inputAll ins
        val _ = TextIO.closeIn ins
        val rawTokens = tokenize content
        val tokens = List.mapPartial mapStringToToken rawTokens
    in
        if List.exists (fn x => x = NONE) (List.map mapStringToToken rawTokens) then (TextIO.print("Parse Error\n"); [])
        else tokens
    end;